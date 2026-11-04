#!/usr/bin/env python3
"""List local PDF and CHM manuals as a draft html-to-md manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from chm_book import discover_topic, hhc_entries, open_chm
from common import (
    PLACEHOLDER_SUMMARY,
    book_key,
    display_name,
    same_book,
    suggest_group,
    suggest_slug,
)
from pdf_book import discover_chapters


def _pdf_books(root: Path) -> list[dict]:
    books = []
    for path in sorted(root.rglob("*.pdf")):
        if path.name.startswith("."):
            continue
        shown = display_name(path.stem).replace("_", " ")
        _meta_title, chapters = discover_chapters(path)
        title = shown
        books.append(
            {
                "slug": suggest_slug(title),
                "title": title,
                "summary": PLACEHOLDER_SUMMARY,
                "group": suggest_group(title, "工具"),
                "kind": "pdf",
                "source": str(path.resolve()),
                "chapters": [{"title": chapter["title"], "page": chapter["page"]} for chapter in chapters],
            }
        )
    return books


def _with_version(title: str, chm_stem: str) -> str:
    folded = title.upper().replace(" ", "")
    if "DM7" in folded or "DM8" in folded:
        return title
    upper = chm_stem.upper()
    if "DM8" in upper:
        return f"DM8 {title}"
    if "DM7" in upper:
        return f"DM7 {title}"
    return title


def _chm_books(root: Path) -> list[dict]:
    books = []
    for path in sorted(root.rglob("*.chm")):
        if path.name.startswith("."):
            continue
        extracted = open_chm(path)
        try:
            entries = hhc_entries(extracted.root)
            folder_names = {entry["group"] for entry in entries if entry["group"]}
            for entry in entries:
                local = entry["local"]
                if not _is_topic(local):
                    continue
                title = entry["title"]
                if title in folder_names or title in {"首页"}:
                    continue
                group = entry["group"]
                if group in {"", "DM7 帮助文档"}:
                    group = "说明"
                chapters = discover_topic(extracted.root, local, title)
                titled = _with_version(title, display_name(path.stem))
                fallback = "工具" if group in {"技术手册", "技术丛书"} else group
                books.append(
                    {
                        "slug": suggest_slug(titled),
                        "title": titled,
                        "summary": PLACEHOLDER_SUMMARY,
                        "group": suggest_group(title, fallback),
                        "kind": "chm",
                        "source": str(path.resolve()),
                        "topic": local,
                        "chapters": [{"title": chapter["title"]} for chapter in chapters],
                    }
                )
        finally:
            extracted.close()
    return books


def _is_topic(local: str) -> bool:
    lowered = local.replace("\\", "/").lower()
    if not lowered.endswith((".htm", ".html")):
        return False
    if ".files/" in lowered or lowered.endswith("header.htm"):
        return False
    return not Path(lowered).name.startswith("~$")


def _dedupe(pdf_books: list[dict], chm_books: list[dict], prefer: str) -> tuple[list[dict], list[dict]]:
    skipped: list[dict] = []
    used_pdf: set[int] = set()
    kept_chm: list[dict] = []
    for chm in chm_books:
        match = None
        for index, pdf in enumerate(pdf_books):
            if index in used_pdf:
                continue
            if same_book(book_key(chm["title"]), book_key(pdf["title"])):
                match = index
                break
        if match is None:
            kept_chm.append(chm)
            continue
        used_pdf.add(match)
        pdf = pdf_books[match]
        if prefer == "chm":
            kept_chm.append(chm)
            skipped.append({**_brief(pdf), "reason": "同一本手册在 CHM 里有 Word HTML，优先用 HTML"})
        else:
            skipped.append({**_brief(chm), "reason": "同一本手册已有 PDF，优先用 PDF 书签"})
    kept_pdf = [pdf for index, pdf in enumerate(pdf_books) if index not in used_pdf]
    if prefer == "pdf":
        books = kept_pdf + kept_chm
    else:
        books = kept_chm + kept_pdf
    _unique_slugs(books)
    return books, skipped


def _brief(book: dict) -> dict:
    brief = {
        "title": book["title"],
        "kind": book["kind"],
        "source": book["source"],
    }
    if book.get("topic"):
        brief["topic"] = book["topic"]
    return brief


def _unique_slugs(books: list[dict]) -> None:
    seen: set[str] = set()
    for book in books:
        slug = book["slug"]
        if slug not in seen:
            seen.add(slug)
            continue
        number = 2
        while f"{slug}-{number}" in seen:
            number += 1
        book["slug"] = f"{slug}-{number}"
        seen.add(book["slug"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Draft a manifest for local PDF and CHM manuals")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--product", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--tags", required=True, help="Comma-separated tags")
    parser.add_argument("--library", required=True, type=Path, help="Library root that will contain catalog.md")
    parser.add_argument("--prefer", choices=("chm", "pdf"), default="chm")
    parser.add_argument("--draft", type=Path, help="Write the draft JSON here instead of stdout")
    args = parser.parse_args()
    if not args.input.is_dir():
        raise SystemExit(f"input is not a directory: {args.input}")
    pdf_books = _pdf_books(args.input)
    chm_books = _chm_books(args.input)
    books, skipped = _dedupe(pdf_books, chm_books, args.prefer)
    draft = {
        "product": args.product,
        "version": args.version,
        "tags": [tag.strip() for tag in args.tags.split(",") if tag.strip()],
        "out": str(args.library.resolve()),
        "books": books,
        "skipped": skipped,
    }
    text = json.dumps(draft, ensure_ascii=False, indent=2) + "\n"
    if args.draft:
        args.draft.parent.mkdir(parents=True, exist_ok=True)
        args.draft.write_text(text, encoding="utf-8")
        print(
            f"books {len(books)} skipped {len(skipped)} chapters {sum(len(book['chapters']) for book in books)} -> {args.draft}",
            flush=True,
        )
        return
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
