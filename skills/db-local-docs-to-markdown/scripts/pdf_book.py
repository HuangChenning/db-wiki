"""Split a text-layer PDF manual on its outline and write Markdown."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import pymupdf

from common import is_contents_title, norm_text

BULLET = re.compile(r"^[\uf000-\uf0ff•·●○■□▪▫►▶‣⁃]+\s*")
END_PUNCT = "。！？；：.?!;"
MONO = 8
BOLD = 16


@dataclass
class Fragment:
    page: int
    y: float
    x: float
    x1: float
    size: float
    flags: int
    kind: str
    text: str
    page_height: float
    display: str = ""
    mono_ratio: float = 0.0
    image: str = ""


@dataclass
class Row:
    page: int
    y: float
    size: float
    flags: int
    kind: str
    text: str
    image: str = ""
    heading_level: int = 0
    parts: list[Fragment] = field(default_factory=list)


@dataclass
class Span:
    title: str
    start_page: int
    end_page: int | None
    end_title: str | None


def open_pdf(path: Path) -> pymupdf.Document:
    document = pymupdf.open(path)
    if document.needs_pass:
        document.close()
        raise SystemExit(f"password-protected PDF: {path}")
    if not _has_text_layer(document):
        document.close()
        raise SystemExit(
            f"no text layer: {path}. This skill does not OCR scanned pages."
        )
    return document


def _has_text_layer(document: pymupdf.Document) -> bool:
    sample = []
    for index in range(min(3, document.page_count)):
        sample.append(document[index].get_text("text"))
    return len("".join(sample).strip()) >= 80


def outline(document: pymupdf.Document) -> list[tuple[int, str, int]]:
    items = []
    for entry in document.get_toc():
        level, title, page = entry[:3]
        title = " ".join(str(title).split())
        if title and page >= 1:
            items.append((int(level), title, int(page)))
    return items


def choose_split_level(items: list[tuple[int, str, int]], override: int | None) -> int:
    if override:
        return override
    for level in range(1, 5):
        kept = [item for item in items if item[0] == level and not is_contents_title(item[1])]
        if len(kept) >= 2:
            return level
    return 1


def chapter_spans(items: list[tuple[int, str, int]], level: int) -> list[Span]:
    bounds = [item for item in items if item[0] == level]
    spans: list[Span] = []
    for index, (item_level, title, page) in enumerate(bounds):
        del item_level
        if is_contents_title(title):
            continue
        nxt = bounds[index + 1] if index + 1 < len(bounds) else None
        spans.append(
            Span(
                title=title,
                start_page=page,
                end_page=nxt[2] if nxt else None,
                end_title=nxt[1] if nxt else None,
            )
        )
    return spans


def discover_chapters(path: Path, split_level: int | None = None) -> tuple[str, list[dict]]:
    document = open_pdf(path)
    try:
        meta_title = " ".join(str((document.metadata or {}).get("title") or "").split())
        items = outline(document)
        level = choose_split_level(items, split_level)
        spans = chapter_spans(items, level) if items else []
        if not spans:
            title = meta_title or display_fallback(path)
            spans = [Span(title=title, start_page=1, end_page=None, end_title=None)]
        chapters = [
            {"title": span.title, "page": span.start_page, "level": level} for span in spans
        ]
        return meta_title, chapters
    finally:
        document.close()


def display_fallback(path: Path) -> str:
    from common import display_name

    return display_name(path.name)


def render_book(
    path: Path,
    *,
    titles: list[str] | None,
    split_level: int | None,
    image_dir: Path,
) -> list[dict]:
    document = open_pdf(path)
    try:
        items = outline(document)
        level = choose_split_level(items, split_level)
        toc_levels = {norm_text(title): item_level for item_level, title, _page in items}
        spans = chapter_spans(items, level) if items else []
        if not spans:
            meta = " ".join(str((document.metadata or {}).get("title") or "").split())
            spans = [Span(title=meta or display_fallback(path), start_page=1, end_page=None, end_title=None)]
        if titles:
            wanted = {norm_text(title) for title in titles}
            spans = [span for span in spans if norm_text(span.title) in wanted]
            found = {norm_text(span.title) for span in spans}
            missing = [title for title in titles if norm_text(title) not in found]
            if missing:
                print(f"WARN {path.name} missing outline entries: {', '.join(missing)}", flush=True)
        rows = _extract_rows(document, image_dir, toc_levels, level)
        rendered = []
        for span in spans:
            body_rows = _slice_rows(rows, span)
            markdown = _rows_to_markdown(body_rows, level)
            if len(markdown.strip()) < 20:
                print(f"WARN empty chapter {span.title!r} in {path.name}", flush=True)
                continue
            rendered.append({"title": span.title, "page": span.start_page, "markdown": markdown})
        if not rendered:
            raise SystemExit(f"no chapters with text in {path.name}")
        return rendered
    finally:
        document.close()


def _extract_rows(
    document: pymupdf.Document,
    image_dir: Path,
    toc_levels: dict[str, int],
    split_level: int,
) -> list[Row]:
    fragments: list[Fragment] = []
    image_index = 0
    for page_index, page in enumerate(document):
        fragments.extend(_page_fragments(page, page_index + 1))
    header_keys = _running_headers(fragments)
    rows: list[Row] = []
    bucket: list[Fragment] = []

    def flush() -> None:
        nonlocal image_index
        if not bucket:
            return
        row = _make_row(bucket, header_keys, toc_levels, split_level)
        bucket.clear()
        if row is None:
            return
        if row.kind == "image":
            image_index += 1
            saved = _save_image(document[row.page - 1], row, image_dir, image_index)
            if saved:
                row.image = saved
                rows.append(row)
            return
        rows.append(row)

    ordered = sorted(fragments, key=lambda item: (item.page, item.y, item.x))
    for fragment in ordered:
        if fragment.kind == "image":
            flush()
            bucket.append(fragment)
            flush()
            continue
        if bucket and (
            fragment.page != bucket[-1].page or abs(fragment.y - bucket[-1].y) > 2.2
        ):
            flush()
        bucket.append(fragment)
    flush()
    return rows


def _page_fragments(page: pymupdf.Page, page_no: int) -> list[Fragment]:
    payload = page.get_text("dict")
    height = float(page.rect.height)
    fragments: list[Fragment] = []
    for block in payload["blocks"]:
        if block.get("type") == 1:
            bbox = tuple(block["bbox"])
            if bbox[2] - bbox[0] < 80 or bbox[3] - bbox[1] < 36:
                continue
            fragments.append(
                Fragment(
                    page=page_no,
                    y=bbox[1],
                    x=bbox[0],
                    x1=bbox[2],
                    size=0,
                    flags=0,
                    kind="image",
                    text="",
                    page_height=height,
                    image=f"{bbox[0]:.1f},{bbox[1]:.1f},{bbox[2]:.1f},{bbox[3]:.1f}",
                )
            )
            continue
        for line in block.get("lines", []):
            spans = [span for span in line.get("spans", []) if span.get("text")]
            if not spans:
                continue
            plain, display, ratio = _format_spans(spans)
            if not plain:
                continue
            bbox = line["bbox"]
            fragments.append(
                Fragment(
                    page=page_no,
                    y=float(bbox[1]),
                    x=float(bbox[0]),
                    x1=float(bbox[2]),
                    size=max(float(span["size"]) for span in spans),
                    flags=int(spans[0]["flags"]),
                    kind="text",
                    text=plain,
                    display=display,
                    mono_ratio=ratio,
                    page_height=height,
                )
            )
    return fragments


def _running_headers(fragments: list[Fragment]) -> set[str]:
    pages: set[int] = set()
    seen: set[tuple[int, str]] = set()
    for fragment in fragments:
        pages.add(fragment.page)
        if fragment.kind != "text" or fragment.y > 72:
            continue
        seen.add((fragment.page, norm_text(fragment.text)))
    counts: Counter[str] = Counter(key for _page, key in seen)
    minimum = max(3, int(len(pages) * 0.4))
    return {key for key, count in counts.items() if count >= minimum and len(key) >= 2}


def _make_row(
    parts: list[Fragment],
    header_keys: set[str],
    toc_levels: dict[str, int],
    split_level: int,
) -> Row | None:
    first = parts[0]
    if first.kind == "image":
        return Row(page=first.page, y=first.y, size=0, flags=0, kind="image", text="", image=first.image)
    parts = sorted(parts, key=lambda item: item.x)
    plain = _join_fragments(parts, "text")
    display = _join_fragments(parts, "display")
    if not plain:
        return None
    text = plain
    if first.y > first.page_height * 0.92 and re.fullmatch(r"\d{1,4}", text):
        return None
    key = norm_text(text)
    if key in header_keys and first.y < 90 and key not in toc_levels:
        return None
    flags = parts[0].flags
    size = max(part.size for part in parts)
    ratio = sum(part.mono_ratio * len(part.text) for part in parts) / max(1, sum(len(part.text) for part in parts))
    level = toc_levels.get(key, 0)
    kind = "text"
    if level and len(plain) <= 80:
        kind = "heading"
        text = plain
    elif size >= 16 and len(plain) <= 40 and ratio < 0.75:
        kind = "heading"
        level = split_level if size >= 20 else split_level + 1
        text = plain
    elif ratio >= 0.75:
        kind = "code"
        text = plain
    else:
        text = display
    text = _clean_bullet(text)
    if kind == "text" and (text.startswith("- ") or re.match(r"^\d+[.、]\s+", text)):
        kind = "list"
    return Row(page=first.page, y=first.y, size=size, flags=flags, kind=kind, text=text, heading_level=level, parts=parts)


def _format_spans(spans: list[dict]) -> tuple[str, str, float]:
    """Return plain text, body text with inline code, and the courier ratio.

    Word manuals set identifiers in Courier inside a SimSun sentence. A line is
    a code block only when most of its characters are Courier; a few identifiers
    stay inline.
    """
    plain_parts: list[str] = []
    display_parts: list[str] = []
    mono = 0
    total = 0
    code_buf: list[str] = []

    def flush_code() -> None:
        if not code_buf:
            return
        raw = "".join(code_buf)
        code_buf.clear()
        stripped = raw.strip().strip("`")
        if len(stripped) < 2 or re.fullmatch(r"\d+[.、]?", stripped):
            display_parts.append(raw)
            return
        lead = raw[: len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()) :]
        display_parts.append(f"{lead}`{stripped}`{trail}")

    for span in spans:
        text = str(span.get("text") or "")
        plain_parts.append(text)
        count = len(text.strip())
        total += count
        font = str(span.get("font") or "").lower()
        if "courier" in font or "consolas" in font or "menlo" in font:
            mono += count
            code_buf.append(text)
        else:
            flush_code()
            display_parts.append(text)
    flush_code()
    ratio = mono / total if total else 0.0
    return "".join(plain_parts).strip(), "".join(display_parts).strip(), ratio


def _join_fragments(parts: list[Fragment], attr: str) -> str:
    pieces: list[str] = []
    previous: Fragment | None = None
    for part in parts:
        chunk = getattr(part, attr).strip()
        if not chunk:
            continue
        if previous is not None:
            gap = part.x - previous.x1
            previous_text = previous.text
            if gap > 12:
                pieces.append("  ")
            elif gap > 1.2 and (previous_text[-1:].isascii() or chunk[:1].isascii()):
                pieces.append(" ")
        pieces.append(chunk)
        previous = part
    return "".join(pieces).strip()


def _clean_bullet(text: str) -> str:
    matched = BULLET.match(text)
    if not matched:
        return text
    rest = text[matched.end() :].strip()
    return f"- {rest}" if rest else "-"


def _save_image(page: pymupdf.Page, row: Row, image_dir: Path, index: int) -> str:
    raw = row.image
    try:
        box = [float(value) for value in raw.split(",")]
    except ValueError:
        return ""
    clip = pymupdf.Rect(box)
    if clip.width < 80 or clip.height < 36:
        return ""
    image_dir.mkdir(parents=True, exist_ok=True)
    name = f"p{row.page}-{index}.png"
    page.get_pixmap(clip=clip, dpi=144, alpha=False).save(image_dir / name)
    row.image = f"img/{name}"
    return row.image


def _slice_rows(rows: list[Row], span: Span) -> list[Row]:
    start = _find_heading(rows, span.title, span.start_page)
    end = _find_heading(rows, span.end_title, span.end_page) if span.end_title else len(rows)
    if start is None:
        start = _first_on_page(rows, span.start_page)
        start = -1 if start is None else start - 1
        print(f"WARN heading not found, using page {span.start_page}: {span.title}", flush=True)
    if span.end_title and end is None:
        end = _first_on_page(rows, span.end_page or span.start_page)
        if end is None:
            end = len(rows)
    return rows[start + 1 : end]


def _find_heading(rows: list[Row], title: str | None, page: int | None) -> int | None:
    if not title:
        return None
    wanted = norm_text(title)
    fallback = None
    for index, row in enumerate(rows):
        if row.kind != "heading" or norm_text(row.text.lstrip("- ")) != wanted:
            continue
        if page is not None and row.page == page:
            return index
        if fallback is None:
            fallback = index
    return fallback


def _first_on_page(rows: list[Row], page: int | None) -> int | None:
    if page is None:
        return None
    for index, row in enumerate(rows):
        if row.page >= page:
            return index
    return None


def _rows_to_markdown(rows: list[Row], split_level: int) -> str:
    blocks: list[str] = []
    paragraph: list[Row] = []
    code: list[str] = []
    lists: list[str] = []

    def flush_paragraph() -> None:
        if not paragraph:
            return
        rows_now = list(paragraph)
        text = _join_paragraph(rows_now)
        paragraph.clear()
        if not text:
            return
        if all(row.flags & BOLD for row in rows_now) and not text.startswith("- "):
            blocks.append(_blockquote(text))
        else:
            blocks.append(text)

    def flush_code() -> None:
        if not code:
            return
        body = "\n".join(code).rstrip()
        code.clear()
        if body:
            blocks.append(f"```\n{body}\n```")

    def flush_list() -> None:
        if not lists:
            return
        blocks.append("\n".join(lists))
        lists.clear()

    for row in rows:
        if row.kind == "heading":
            flush_paragraph()
            flush_code()
            flush_list()
            level = row.heading_level or (split_level + 1)
            hashes = max(2, min(6, level - split_level + 1))
            blocks.append(f"{'#' * hashes} {row.text}")
            continue
        if row.kind == "image":
            flush_paragraph()
            flush_code()
            flush_list()
            blocks.append(f"![]({row.image})")
            continue
        if row.kind == "code":
            flush_paragraph()
            flush_list()
            code.append(row.text)
            continue
        if row.kind == "list":
            flush_paragraph()
            flush_code()
            lists.append(row.text)
            continue
        flush_code()
        flush_list()
        if paragraph and _new_paragraph(paragraph[-1], row):
            flush_paragraph()
        paragraph.append(row)
    flush_paragraph()
    flush_code()
    flush_list()
    return _tidy_gaps("\n\n".join(blocks).strip() + "\n")


def _new_paragraph(previous: Row, row: Row) -> bool:
    if row.text.startswith("- ") or re.match(r"^\d+[.、]\s*", row.text):
        return True
    if previous.text.startswith("- ") and len(previous.text) < 40:
        return True
    if previous.text[-1:] in END_PUNCT:
        return True
    if abs(row.size - previous.size) > 1.5:
        return True
    return False


def _join_paragraph(rows: list[Row]) -> str:
    if not rows:
        return ""
    text = rows[0].text
    for row in rows[1:]:
        text = _join_text(text, row.text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", "", text)
    text = re.sub(r"`\s+(?=[\u4e00-\u9fff（）])", "`", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff（）])\s+`", "`", text)
    text = re.sub(r"(?<![A-Za-z0-9`])([A-Za-z])\s+(?=[\u4e00-\u9fff])", r"\1", text)
    text = re.sub(r"\s+([，。！？；：、])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def _join_text(left: str, right: str) -> str:
    if not left:
        return right
    if not right:
        return left
    if "\u4e00" <= left[-1] <= "\u9fff" and "\u4e00" <= right[0] <= "\u9fff":
        return left + right
    if left[-1].isascii() and left[-1].isalnum() and right[0].isascii() and right[0].isalnum():
        return left + " " + right
    return left + right


def _blockquote(text: str) -> str:
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def _tidy_gaps(markdown: str) -> str:
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown
