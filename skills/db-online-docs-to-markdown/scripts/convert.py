#!/usr/bin/env python3
"""Convert a manifest of database HTML chapters into an html-to-md library."""

from __future__ import annotations

import argparse
import gzip
import json
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import unquote, urlparse

USER_AGENT = "Mozilla/5.0"
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
PAGE = re.compile(r"^(?:[A-Za-z0-9_+-]+/)*[A-Za-z0-9_+-]+\.html?$")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
DESC_AFTER = re.compile(r"\s*\[[^\]]*\]\((https?://[^)\s]*?/img_text/[^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_LINE = re.compile(r"\[Go to main content\]\(#BEGIN\)\n?")
GENERIC_ALT = {"删除目录", "image", "img", "picture", "图片", "Image"}
GENERIC_TITLE = {"达梦技术文档"}
IMAGE_LOCK = threading.Lock()


def _yaml_value(value: str) -> str:
    if value and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 ._()/-]*", value):
        return value
    return json.dumps(value, ensure_ascii=False)


def _read_url(url: str) -> bytes:
    last: Exception | None = None
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except Exception as exc:
            last = exc
            time.sleep(attempt + 1)
    assert last is not None
    raise last


def _http_status(url: str) -> str:
    try:
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(request, timeout=60) as response:
            return str(response.status)
    except urllib.error.HTTPError as exc:
        return str(exc.code)
    except Exception as exc:
        return type(exc).__name__


def _run_defuddle(url: str) -> dict:
    last: Exception | None = None
    completed = None
    for attempt in range(3):
        try:
            completed = subprocess.run(
                ["defuddle", "parse", url, "--md", "--json"],
                check=False,
                capture_output=True,
                text=True,
                timeout=180,
            )
        except subprocess.TimeoutExpired as exc:
            last = exc
            time.sleep(attempt + 1)
            continue
        if completed.returncode == 0:
            break
        last = OSError(completed.stderr.strip() or f"defuddle exited {completed.returncode}")
        time.sleep(attempt + 1)
    if completed is None or completed.returncode != 0:
        raise OSError(str(last) if last else f"defuddle failed for {url}")
    payload = json.loads(completed.stdout)
    if not isinstance(payload, dict) or not isinstance(payload.get("content"), str):
        raise OSError(f"defuddle returned no content for {url}")
    if not isinstance(payload.get("title"), str):
        payload["title"] = ""
    return payload


def _image_bytes(data: bytes) -> bytes:
    if data[:2] == b"\x1f\x8b":
        return gzip.decompress(data)
    return data


def _image_suffix(data: bytes) -> str | None:
    if data.startswith(b"\x89PNG"):
        return ".png"
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data.startswith(b"GIF8"):
        return ".gif"
    if data.startswith(b"RIFF") and len(data) >= 12 and data[8:12] == b"WEBP":
        return ".webp"
    if data.startswith(b"BM"):
        return ".bmp"
    stripped = data.lstrip()
    if stripped.startswith((b"<!DOCTYPE", b"<html", b"<!doctype", b"<HTML")):
        return None
    return ""


def _image_name(url: str) -> str:
    if url.startswith("data:"):
        return "image.bin"
    name = unquote(urlparse(url).path.rsplit("/", 1)[-1]).strip()
    name = name.replace("/", "_").replace("\\", "_")
    if not name or name in {".", ".."}:
        name = "image.bin"
    return name


def _caption_before(md: str, pos: int) -> str | None:
    for line in reversed(md[:pos].splitlines()):
        stripped = line.strip()
        if not stripped or stripped.startswith("![") or "/img_text/" in stripped:
            continue
        if stripped.startswith("Figure ") or stripped.startswith("图"):
            return stripped
        return None
    return None


def _blockquote(text: str) -> str:
    return "\n".join(f"> {line}" if line else ">" for line in text.strip().splitlines())


def _load_image(url: str, fetch_bytes: Callable[[str], bytes]) -> bytes:
    if url.startswith("data:"):
        header, _, encoded = url.partition(",")
        if ";base64" not in header:
            raise OSError("image data uri is not base64")
        import base64

        return base64.b64decode(encoded)
    return _image_bytes(fetch_bytes(url))


def rewrite_markdown(
    md: str,
    *,
    page_url: str,
    base_url: str,
    image_dir: Path,
    fetch_bytes: Callable[[str], bytes],
    fetch_text: Callable[[str], str] | None = None,
) -> str:
    md = SKIP_LINE.sub("", md)
    image_error: Exception | None = None
    for match in reversed(list(IMAGE.finditer(md))):
        url = match.group(2)
        if url.startswith(("img/", "./img/")):
            continue
        if not url.startswith(("http://", "https://", "data:")):
            continue
        name = _image_name(url)
        try:
            with IMAGE_LOCK:
                existing = list(image_dir.glob(name + "*")) if image_dir.is_dir() else []
            if existing:
                name = existing[0].name
            else:
                data = _load_image(url, fetch_bytes)
                suffix = _image_suffix(data)
                if suffix is None:
                    md = md[: match.start()] + md[match.end() :]
                    continue
                if suffix and not name.lower().endswith(suffix):
                    stem = name.rsplit(".", 1)[0] if "." in name else name
                    name = f"{stem}{suffix}"
                dest = image_dir / name
                with IMAGE_LOCK:
                    if not dest.is_file():
                        image_dir.mkdir(parents=True, exist_ok=True)
                        dest.write_bytes(data)
        except OSError as exc:
            image_error = exc
            continue
        alt = match.group(1).strip()
        if alt.startswith("Description of"):
            alt = ""
        if not alt or alt in GENERIC_ALT:
            alt = _caption_before(md, match.start()) or Path(name).stem
        image_md = f"![{alt}](img/{name})"
        desc = DESC_AFTER.match(md, match.end())
        if desc is not None and fetch_text is not None:
            try:
                image_md = f"{image_md}\n\n{_blockquote(fetch_text(desc.group(1)))}\n"
                md = md[: match.start()] + image_md + md[desc.end() :]
                continue
            except OSError:
                pass
        md = md[: match.start()] + image_md + md[match.end() :]
    if image_error is not None:
        raise image_error

    page_name = urlparse(page_url).path.rsplit("/", 1)[-1]
    section_path = urlparse(base_url).path

    def replace_link(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        if url.startswith("#"):
            return label
        path = url
        if url.startswith(base_url):
            path = url[len(base_url) :].split("#", 1)[0]
        elif url.startswith(("http://", "https://")):
            parsed = urlparse(url)
            if parsed.netloc == urlparse(base_url).netloc and parsed.path.startswith(section_path):
                path = unquote(parsed.path[len(section_path) :]).split("#", 1)[0]
            else:
                return match.group(0)
        else:
            path = unquote(url.split("#", 1)[0])
            if path.startswith("./"):
                path = path[2:]
        if path.startswith(("img/", "images/", "img_text/")) or PAGE.fullmatch(path) is None:
            return match.group(0)
        if path.rsplit("/", 1)[-1] == page_name:
            return label
        return f"[{label}]({path.rsplit('/', 1)[-1].rsplit('.', 1)[0]}.md)"

    return LINK.sub(replace_link, md)


def _stem(chapter: dict) -> str:
    if chapter.get("stem"):
        return str(chapter["stem"])
    return Path(str(chapter["href"])).name.rsplit(".", 1)[0]


def load_manifest(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("manifest must be an object")
    for key in ("product", "version", "tags", "out", "books"):
        if key not in data:
            raise SystemExit(f"manifest missing {key}")
    out = Path(data["out"])
    if out.name != "html-to-md":
        raise SystemExit(f"out directory must be named html-to-md, got {out}")
    if not isinstance(data["tags"], list) or not data["tags"]:
        raise SystemExit("tags must be a non-empty list")
    slugs: set[str] = set()
    for book in data["books"]:
        slug = book.get("slug", "")
        if SLUG.fullmatch(slug) is None:
            raise SystemExit(f"bad slug {slug!r}")
        if slug in slugs:
            raise SystemExit(f"duplicate slug {slug}")
        slugs.add(slug)
        for key in ("title", "summary", "group", "base_url", "chapters"):
            if not book.get(key):
                raise SystemExit(f"{slug} missing {key}")
        if not str(book["base_url"]).endswith("/"):
            raise SystemExit(f"{slug} base_url must end with /")
        stems: set[str] = set()
        for chapter in book["chapters"]:
            href = str(chapter.get("href", ""))
            title = str(chapter.get("title", "")).strip()
            if PAGE.fullmatch(href) is None or href.startswith("/"):
                raise SystemExit(f"{slug} bad href {href!r}")
            if not title:
                raise SystemExit(f"{slug} chapter {href} missing title")
            stem = _stem(chapter)
            if stem in stems:
                raise SystemExit(f"{slug} duplicate file stem {stem}")
            stems.add(stem)
    return data


def _render_note(*, title: str, book: dict, manifest: dict, source_url: str, body: str) -> str:
    lines = [
        "---",
        f"title: {_yaml_value(title)}",
        f"book: {_yaml_value(book['title'])}",
    ]
    if book.get("doc_id"):
        lines.append(f"doc_id: {_yaml_value(str(book['doc_id']))}")
    lines.append(f"version: {json.dumps(str(manifest['version']), ensure_ascii=False)}")
    lines.append(f"source: {json.dumps(source_url, ensure_ascii=False)}")
    lines.append("tags:")
    for tag in list(manifest["tags"]) + [book["slug"]]:
        lines.append(f"  - {tag}")
    lines.append("---")
    lines.append("")
    lines.append(body.lstrip())
    return "\n".join(lines)


def _chapter_url(base_url: str, href: str) -> str:
    return base_url + href


def convert(manifest: dict, *, workers: int, force: bool) -> int:
    out = Path(manifest["out"])
    failures = 0
    for book in manifest["books"]:
        slug = book["slug"]
        book_dir = out / slug
        image_dir = book_dir / "img"
        book_dir.mkdir(parents=True, exist_ok=True)
        chapters = book["chapters"]
        print(f"== {slug} {len(chapters)}", flush=True)

        def write_chapter(chapter: dict) -> bool:
            href = str(chapter["href"])
            stem = _stem(chapter)
            path = book_dir / f"{stem}.md"
            if not force and path.is_file() and path.stat().st_size > 0:
                return True
            source_url = _chapter_url(book["base_url"], href)
            try:
                payload = _run_defuddle(source_url)
                note_title = str(payload.get("title") or "").strip()
                if not note_title or note_title == book["title"] or note_title in GENERIC_TITLE:
                    note_title = str(chapter["title"])
                body = rewrite_markdown(
                    str(payload.get("content") or ""),
                    page_url=source_url,
                    base_url=book["base_url"],
                    image_dir=image_dir,
                    fetch_bytes=_read_url,
                    fetch_text=lambda url: str(_run_defuddle(url).get("content") or ""),
                )
            except Exception as exc:
                print(f"FAIL {slug}/{href}: {exc} (HTTP {_http_status(source_url)})", file=sys.stderr, flush=True)
                return False
            if not body.strip() or body.strip() in {"No content", "JavaScript must be enabled"}:
                print(f"SKIP {slug}/{href}: empty", file=sys.stderr, flush=True)
                return False
            path.write_text(
                _render_note(
                    title=note_title,
                    book=book,
                    manifest=manifest,
                    source_url=source_url,
                    body=body,
                ),
                encoding="utf-8",
            )
            print(path, flush=True)
            return True

        with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            results = list(pool.map(write_chapter, chapters))
        failures += results.count(False)
        print(f"done {slug}", flush=True)
    _write_indexes(manifest)
    return failures


def _write_indexes(manifest: dict) -> None:
    out = Path(manifest["out"])
    grouped: dict[str, list[dict]] = {}
    for book in manifest["books"]:
        grouped.setdefault(book["group"], []).append(book)
    parts = [
        "---\n",
        f"title: {_yaml_value(manifest['product'] + ' 文档目录')}\n",
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
    for group, books in grouped.items():
        parts.append(f"\n## {group}\n\n")
        for book in books:
            summary = str(book["summary"]).strip().rstrip("。")
            parts.append(f"- `{book['slug']}/contents.md`：{book['title']}。{summary}。\n")
            lines = []
            for chapter in book["chapters"]:
                stem = _stem(chapter)
                if not (out / book["slug"] / f"{stem}.md").is_file():
                    continue
                label = str(chapter["title"]).replace("]", "")
                lines.append(f"- [{label}]({stem}.md)")
            link_count += len(lines)
            contents = (
                "---\n"
                f"title: {_yaml_value(book['title'] + ' 目录')}\n"
                f"book: {_yaml_value(book['title'])}\n"
                f"version: {json.dumps(str(manifest['version']), ensure_ascii=False)}\n"
                "tags:\n"
                + "".join(f"  - {tag}\n" for tag in list(manifest["tags"]) + [book["slug"], "contents"])
                + "---\n\n"
                f"# {book['title']}\n\n"
                "按原站点顺序排列。路径相对于本目录。\n\n"
                + "\n".join(lines)
                + "\n"
            )
            target = out / book["slug"]
            target.mkdir(parents=True, exist_ok=True)
            (target / "contents.md").write_text(contents, encoding="utf-8")
            print(f"contents {book['slug']} {len(lines)}", flush=True)
    (out / "catalog.md").write_text("".join(parts), encoding="utf-8")
    print(f"catalog books {len(manifest['books'])} links {link_count}", flush=True)


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
        slug = book["slug"]
        contents = out / slug / "contents.md"
        if contents.is_file():
            for link in re.findall(r"\]\(([^)]+\.md)\)", contents.read_text(encoding="utf-8")):
                if not (out / slug / link).is_file():
                    problems.append(f"contents link missing {slug}/{link}")
        for chapter in book["chapters"]:
            stem = _stem(chapter)
            note = out / slug / f"{stem}.md"
            if not note.is_file() or note.stat().st_size == 0:
                problems.append(f"missing {slug}/{stem}.md")
                continue
            text = note.read_text(encoding="utf-8")
            for match in IMAGE.finditer(text):
                url = match.group(2)
                if not url.startswith("img/"):
                    problems.append(f"{slug}/{stem}.md image not local: {url}")
                    continue
                image = out / slug / url
                if not image.is_file():
                    problems.append(f"missing {slug}/{url}")
                    continue
                blob = image.read_bytes()[:16]
                if blob[:2] == b"\x1f\x8b":
                    problems.append(f"gzip image {slug}/{url}")
                elif blob.lstrip().startswith((b"<!DOCTYPE", b"<html", b"<!doctype", b"<HTML")):
                    problems.append(f"html image {slug}/{url}")
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
        count = len(book["chapters"])
        total += count
        print(f"{book['group']}\t{book['slug']}\t{count}\t{book['title']}")
    print(f"books {len(manifest['books'])} chapters {total}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a database HTML manifest to Markdown")
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    manifest = load_manifest(args.manifest)
    if args.dry_run:
        dry_run(manifest)
        return
    if not args.verify:
        if shutil_which("defuddle") is None:
            raise SystemExit("defuddle is not on PATH")
        failures = convert(manifest, workers=args.workers, force=args.force)
        if failures:
            print(f"failures {failures}", file=sys.stderr)
            raise SystemExit(1)
    if args.verify or not args.dry_run:
        if args.verify:
            raise SystemExit(verify(manifest))


def shutil_which(name: str) -> str | None:
    import shutil

    return shutil.which(name)


if __name__ == "__main__":
    main()
