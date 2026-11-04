#!/usr/bin/env python3
"""Convert a manifest of local PDF and CHM manuals into an html-to-md library."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from chm_book import open_chm, render_topic
from common import assign_stems, load_manifest, source_ref, yaml_value
from pdf_book import render_book

IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def _selected(manifest: dict, only: str | None) -> list[dict]:
    books = []
    for book in manifest["books"]:
        if book.get("skip"):
            continue
        if only and book["slug"] != only:
            continue
        books.append(book)
    if only and not books:
        raise SystemExit(f"no book with slug {only}")
    return books


def convert(manifest: dict, *, force: bool, only: str | None) -> int:
    out = Path(manifest["out"])
    failures = 0
    chm_cache: dict[str, object] = {}
    try:
        for book in _selected(manifest, only):
            slug = book["slug"]
            book_dir = out / slug
            image_dir = book_dir / "img"
            book_dir.mkdir(parents=True, exist_ok=True)
            print(f"== {slug}", flush=True)
            try:
                rendered = _render(book, image_dir, chm_cache)
            except (Exception, SystemExit) as exc:
                print(f"FAIL {slug}: {exc}", file=sys.stderr, flush=True)
                failures += 1
                continue
            by_title = { _key(item["title"]): item for item in rendered }
            chapters = list(book.get("chapters") or [])
            if not chapters:
                chapters = [{"title": item["title"]} for item in rendered]
            else:
                missing = [chapter["title"] for chapter in chapters if _key(chapter["title"]) not in by_title]
                if missing:
                    print(f"WARN {slug} dropped empty chapters: {', '.join(missing)}", flush=True)
                    chapters = [chapter for chapter in chapters if _key(chapter["title"]) in by_title]
            if not chapters:
                print(f"FAIL {slug}: no chapters", file=sys.stderr, flush=True)
                failures += 1
                continue
            assign_stems(chapters)
            book["chapters"] = chapters
            for chapter in chapters:
                item = by_title[_key(chapter["title"])]
                path = book_dir / f"{chapter['stem']}.md"
                if not force and path.is_file() and path.stat().st_size > 0:
                    print(path, flush=True)
                    continue
                path.write_text(
                    _render_note(title=str(chapter["title"]), book=book, manifest=manifest, item=item),
                    encoding="utf-8",
                )
                print(path, flush=True)
    finally:
        for extracted in chm_cache.values():
            extracted.close()
    if failures:
        return failures
    if only:
        return 0
    _write_indexes(manifest)
    return 0


def _render(book: dict, image_dir: Path, chm_cache: dict) -> list[dict]:
    source = Path(book["source"])
    titles = [str(chapter["title"]) for chapter in book.get("chapters") or []]
    fallback = titles[0] if len(titles) == 1 else str(book["title"])
    if book["kind"] == "pdf":
        return render_book(
            source,
            titles=titles or None,
            split_level=book.get("split_level"),
            image_dir=image_dir,
        )
    extracted = chm_cache.get(str(source))
    if extracted is None:
        extracted = open_chm(source)
        chm_cache[str(source)] = extracted
    return render_topic(
        extracted.root,
        topic=str(book["topic"]),
        fallback_title=fallback,
        titles=titles or None,
        image_dir=image_dir,
    )


def _key(title: str) -> str:
    return "".join(str(title).split()).lower()


def _render_note(*, title: str, book: dict, manifest: dict, item: dict) -> str:
    source = Path(book["source"])
    if book["kind"] == "pdf":
        suffix = f"#page={item.get('page', 1)}"
    else:
        suffix = "#" + str(book["topic"])
    lines = [
        "---",
        f"title: {yaml_value(title)}",
        f"book: {yaml_value(book['title'])}",
        f"version: {json.dumps(str(manifest['version']), ensure_ascii=False)}",
        f"source: {json.dumps(source_ref(source, suffix), ensure_ascii=False)}",
        "tags:",
    ]
    for tag in list(manifest["tags"]) + [book["slug"]]:
        lines.append(f"  - {tag}")
    lines.extend(["---", "", item["markdown"].lstrip()])
    return "\n".join(lines)


def _write_indexes(manifest: dict) -> None:
    out = Path(manifest["out"])
    grouped: dict[str, list[dict]] = {}
    books = [book for book in manifest["books"] if not book.get("skip")]
    for book in books:
        grouped.setdefault(book["group"], []).append(book)
    parts = [
        "---\n",
        f"title: {yaml_value(manifest['product'] + ' 文档目录')}\n",
        f"version: {json.dumps(str(manifest['version']), ensure_ascii=False)}\n",
        "tags:\n",
    ]
    for tag in list(manifest["tags"]) + ["catalog"]:
        parts.append(f"  - {tag}\n")
    parts.append(
        "---\n\n"
        f"# {manifest['product']} 文档目录\n\n"
        "路径都相对于本文件所在的 `html-to-md` 目录。检索时先选定一栏，再打开对应的 `contents.md`。\n"
    )
    link_count = 0
    for group, group_books in grouped.items():
        parts.append(f"\n## {group}\n\n")
        for book in group_books:
            summary = str(book["summary"]).strip().rstrip("。")
            parts.append(f"- `{book['slug']}/contents.md`：{book['title']}。{summary}。\n")
            lines = []
            for chapter in book.get("chapters") or []:
                stem = chapter.get("stem")
                if not stem or not (out / book["slug"] / f"{stem}.md").is_file():
                    continue
                label = str(chapter["title"]).replace("]", "")
                lines.append(f"- [{label}]({stem}.md)")
            link_count += len(lines)
            contents = (
                "---\n"
                f"title: {yaml_value(book['title'] + ' 目录')}\n"
                f"book: {yaml_value(book['title'])}\n"
                f"version: {json.dumps(str(manifest['version']), ensure_ascii=False)}\n"
                "tags:\n"
                + "".join(f"  - {tag}\n" for tag in list(manifest["tags"]) + [book["slug"], "contents"])
                + "---\n\n"
                f"# {book['title']}\n\n"
                "按原书顺序排列。路径相对于本目录。\n\n"
                + "\n".join(lines)
                + "\n"
            )
            target = out / book["slug"]
            target.mkdir(parents=True, exist_ok=True)
            (target / "contents.md").write_text(contents, encoding="utf-8")
            print(f"contents {book['slug']} {len(lines)}", flush=True)
    (out / "catalog.md").write_text("".join(parts), encoding="utf-8")
    print(f"catalog books {len(books)} links {link_count}", flush=True)


def verify(manifest: dict) -> int:
    out = Path(manifest["out"])
    problems: list[str] = []
    catalog = out / "catalog.md"
    if not catalog.is_file():
        problems.append("missing catalog.md")
    else:
        text = catalog.read_text(encoding="utf-8")
        if "http://" in text or "https://" in text:
            problems.append("catalog.md contains an absolute URL")
        if "/Users/" in text or "/home/" in text:
            problems.append("catalog.md contains a filesystem path")
    for book in manifest["books"]:
        if book.get("skip"):
            continue
        slug = book["slug"]
        contents = out / slug / "contents.md"
        if contents.is_file():
            for link in re.findall(r"\]\(([^)]+\.md)\)", contents.read_text(encoding="utf-8")):
                if not (out / slug / link).is_file():
                    problems.append(f"contents link missing {slug}/{link}")
        chapters = [dict(chapter) for chapter in book.get("chapters") or []]
        assign_stems(chapters)
        for chapter in chapters:
            stem = chapter.get("stem")
            if not stem:
                problems.append(f"{slug} chapter has no stem")
                continue
            note = out / slug / f"{stem}.md"
            if not note.is_file() or note.stat().st_size == 0:
                problems.append(f"missing {slug}/{stem}.md")
                continue
            text = note.read_text(encoding="utf-8")
            if "source:" not in text.split("---", 2)[1]:
                problems.append(f"{slug}/{stem}.md missing source")
            for match in IMAGE.finditer(text):
                url = match.group(2)
                if not url.startswith("img/"):
                    problems.append(f"{slug}/{stem}.md image not local: {url}")
                    continue
                image = out / slug / url
                if not image.is_file():
                    problems.append(f"missing {slug}/{url}")
    if problems:
        for item in problems:
            print(item, file=sys.stderr)
        print(f"verify failed {len(problems)}", file=sys.stderr)
        return 1
    print("verify ok")
    return 0


def dry_run(manifest: dict) -> None:
    total = 0
    for book in manifest["books"]:
        if book.get("skip"):
            continue
        count = len(book.get("chapters") or [])
        total += count
        print(f"{book['group']}\t{book['kind']}\t{book['slug']}\t{count}\t{book['title']}")
    print(f"books {sum(1 for book in manifest['books'] if not book.get('skip'))} chapters {total}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert local PDF and CHM manuals to Markdown")
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--only", help="Convert a single slug and skip catalog rebuild")
    args = parser.parse_args()
    manifest = load_manifest(args.manifest)
    if args.dry_run:
        dry_run(manifest)
        return
    if not args.verify:
        failures = convert(manifest, force=args.force, only=args.only)
        if failures:
            print(f"failures {failures}", file=sys.stderr)
            raise SystemExit(1)
    if args.verify:
        raise SystemExit(verify(manifest))


if __name__ == "__main__":
    main()
