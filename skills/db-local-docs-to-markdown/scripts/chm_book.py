"""Extract a CHM help file with 7-Zip and convert its Word HTML topics."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from lxml import html as lhtml
from lxml.html import HtmlElement

from common import is_contents_title, norm_text

HHC_TOKEN = re.compile(r"<UL>|</UL>|<OBJECT\b.*?</OBJECT>", re.I | re.S)
NAME_PARAM = re.compile(r'name="Name"\s+value="([^"]*)"', re.I)
LOCAL_PARAM = re.compile(r'name="Local"\s+value="([^"]*)"', re.I)
SKIP_TAGS = {"script", "style", "head", "meta", "link", "title"}
CODE_FONTS = ("courier", "consolas", "lucida console", "source code")
ASCII_RUN = re.compile(r"[A-Za-z0-9_./\\:+#@-]+")
VML_SRC = re.compile(r'src="([^"]+\.(?:png|jpe?g|gif|webp|bmp))"', re.I)
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}


def extract_chm(path: Path, dest: Path) -> None:
    if shutil.which("7z") is None:
        raise SystemExit("7z is not on PATH. Install p7zip and retry.")
    dest.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        ["7z", "x", "-y", f"-o{dest}", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout or "").strip()
        raise SystemExit(f"7z failed for {path}: {detail}")


class Extracted:
    def __init__(self, root: Path, own: tempfile.TemporaryDirectory[str] | None) -> None:
        self.root = root
        self._own = own

    def close(self) -> None:
        if self._own is not None:
            self._own.cleanup()


def open_chm(path: Path) -> Extracted:
    temporary = tempfile.TemporaryDirectory(prefix="chm-")
    root = Path(temporary.name)
    try:
        extract_chm(path, root)
    except Exception:
        temporary.cleanup()
        raise
    return Extracted(root, temporary)


def hhc_entries(root: Path) -> list[dict]:
    files = list(root.rglob("*.hhc"))
    if not files:
        raise SystemExit(f"no .hhc contents file under {root}")
    text = _decode(files[0].read_bytes())
    parent = [""]
    last_name = ""
    entries: list[dict] = []
    for match in HHC_TOKEN.finditer(text):
        token = match.group(0)
        upper = token.upper()
        if upper == "<UL>":
            parent.append(last_name)
            continue
        if upper == "</UL>":
            if len(parent) > 1:
                parent.pop()
            continue
        name_match = NAME_PARAM.search(token)
        local_match = LOCAL_PARAM.search(token)
        if not name_match or not local_match:
            continue
        last_name = " ".join(name_match.group(1).split())
        local = local_match.group(1).replace("\\", "/").strip()
        group = parent[-1] or "说明"
        entries.append({"title": last_name, "local": local, "group": group})
    return entries


def discover_topic(root: Path, topic: str, fallback_title: str) -> list[dict]:
    path = _topic_path(root, topic)
    document = _parse_html(path)
    body = document.find("body")
    if body is None:
        body = document
    titles = []
    for element in body.iter():
        if _local(element.tag) != "h1":
            continue
        title = _clean("".join(element.itertext()))
        if title and not is_contents_title(title):
            titles.append(title)
    if not titles:
        titles.append(fallback_title)
    return [{"title": title} for title in titles]


def render_topic(
    root: Path,
    *,
    topic: str,
    fallback_title: str,
    titles: list[str] | None,
    image_dir: Path,
) -> list[dict]:
    path = _topic_path(root, topic)
    document = _parse_html(path)
    body = document.find("body")
    if body is None:
        body = document
    image_index = 0

    def take_image(src: str) -> str:
        nonlocal image_index
        image_index += 1
        return _copy_image(src, path, image_dir, image_index)

    blocks = _walk(body, take_image)
    chapters = _split_chapters(blocks, fallback_title)
    if titles:
        wanted = {norm_text(title) for title in titles}
        chapters = [chapter for chapter in chapters if norm_text(chapter["title"]) in wanted]
        found = {norm_text(chapter["title"]) for chapter in chapters}
        missing = [title for title in titles if norm_text(title) not in found]
        if missing:
            print(f"WARN {topic} missing headings: {', '.join(missing)}", flush=True)
    rendered = []
    for chapter in chapters:
        markdown = _blocks_to_markdown(chapter["blocks"]).strip()
        if len(markdown) < 20:
            print(f"WARN empty chapter {chapter['title']!r} in {topic}", flush=True)
            continue
        rendered.append({"title": chapter["title"], "markdown": markdown + "\n"})
    if not rendered:
        raise SystemExit(f"no chapters with text in {topic}")
    return rendered


def _topic_path(root: Path, topic: str) -> Path:
    relative = Path(topic.replace("\\", "/"))
    candidate = root / relative
    if candidate.is_file():
        return candidate
    matches = [item for item in root.rglob(relative.name) if item.is_file()]
    if len(matches) == 1:
        return matches[0]
    raise SystemExit(f"topic not in CHM: {topic}")


def _decode(data: bytes) -> str:
    head = data[:2500].lower()
    if data[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return data.decode("utf-16")
    if b"charset=gb" in head or b"charset=\"gb" in head:
        return data.decode("gb18030", errors="replace")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("gb18030", errors="replace")


def _parse_html(path: Path) -> HtmlElement:
    return lhtml.fromstring(_decode(path.read_bytes()))


def _local(tag: object) -> str:
    if not isinstance(tag, str):
        return ""
    if "}" in tag:
        tag = tag.rsplit("}", 1)[-1]
    return tag.lower()


def _clean(value: str) -> str:
    value = re.sub(r"<!\[endif\]>|\[if[^\]]*\]|\[endif\]", "", value, flags=re.I)
    value = re.sub(r"</?[A-Za-z][^>\n]{0,300}>", "", value)
    value = " ".join(value.replace("\xa0", " ").split())
    return re.sub(r"^(?:[ln]|ü|Ø|●)\s+", "- ", value)


def _src_of(element: HtmlElement) -> str:
    for key, value in element.attrib.items():
        name = key.rsplit("}", 1)[-1].lower()
        if name in {"src", "href"} and value and not value.startswith("#"):
            return value
    return ""


def _walk(element: HtmlElement, take_image) -> list[dict]:
    blocks: list[dict] = []
    tag = _local(element.tag)
    if tag in SKIP_TAGS or tag == "":
        return blocks
    if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        title = _clean("".join(element.itertext()))
        if title:
            blocks.append({"kind": "h", "level": int(tag[1]), "text": title})
        return blocks
    if tag == "table":
        table = _table(element)
        if table:
            blocks.append({"kind": "table", "text": table})
        return blocks
    if tag == "pre":
        text = "\n".join(line.rstrip() for line in "".join(element.itertext()).splitlines()).strip("\n")
        if text.strip():
            blocks.append({"kind": "code", "text": text})
        return blocks
    if tag in {"ul", "ol"}:
        text = _list(element, ordered=tag == "ol")
        if text:
            blocks.append({"kind": "list", "text": text})
        return blocks
    if tag in {"img", "imagedata"}:
        saved = take_image(_src_of(element))
        if saved:
            blocks.append({"kind": "image", "text": saved})
        return blocks
    if tag == "p":
        blocks.extend(_paragraph(element, take_image))
        return blocks
    if element.text and element.text.strip() and tag not in {"div", "body", "html", "span", "font"}:
        blocks.append({"kind": "p", "text": _clean(element.text)})
    for child in element:
        blocks.extend(_walk(child, take_image))
    return blocks


def _vml_sources(element: HtmlElement) -> list[str]:
    chunks: list[str] = []
    for node in element.iter():
        for value in (node.text, node.tail):
            if value and _is_vml(value):
                chunks.append(value)
    seen: set[str] = set()
    sources: list[str] = []
    for src in VML_SRC.findall("\n".join(chunks)):
        if src not in seen:
            seen.add(src)
            sources.append(src)
    return sources


def _style_blob(element: HtmlElement) -> str:
    return f"{element.get('style') or ''} {element.get('class') or ''}".lower()


def _paragraph(element: HtmlElement, take_image) -> list[dict]:
    blocks: list[dict] = []
    pieces: list[tuple[bool, str]] = []

    def flush() -> None:
        if not pieces:
            return
        block = _text_from_pieces(element, pieces)
        pieces.clear()
        if block:
            blocks.append(block)

    for src in _vml_sources(element):
        saved = take_image(src)
        if saved:
            blocks.append({"kind": "image", "text": saved})
    if element.text and not _is_vml(element.text):
        pieces.extend(_classify_text(element.text, full=_full_code(_style_blob(element)), ascii_code=False))
    for child in element:
        child_tag = _local(child.tag)
        if child_tag in {"img", "imagedata"}:
            flush()
            saved = take_image(_src_of(child))
            if saved:
                blocks.append({"kind": "image", "text": saved})
        else:
            pieces.extend(_pieces(child, _full_code(_style_blob(element))))
        if child.tail and not _is_vml(child.tail):
            pieces.extend(
                _classify_text(child.tail, full=_full_code(_style_blob(element)), ascii_code=False)
            )
    flush()
    return blocks


def _pieces(element: HtmlElement, inherited: bool) -> list[tuple[bool, str]]:
    if _local(element.tag) in {"img", "imagedata", "shapetype", "shape", "stroke", "formulas", "path", "lock"}:
        return []
    style = f"{element.get('style') or ''} {element.get('class') or ''}".lower()
    full = inherited or _full_code(style)
    ascii_code = not full and _ascii_font_is_code(style)
    pieces: list[tuple[bool, str]] = []
    pieces.extend(_classify_text(element.text or "", full=full, ascii_code=ascii_code))
    for child in element:
        pieces.extend(_pieces(child, full))
        pieces.extend(_classify_text(child.tail or "", full=full, ascii_code=ascii_code))
    return pieces


def _full_code(style: str) -> bool:
    main = re.sub(
        r"mso-(?:ascii|hansi|fareast|bidi)-font-family:\s*(?:\"[^\"]*\"|'[^']*'|[^;]+)",
        "",
        style,
    )
    return any(font in main for font in CODE_FONTS) or "msoplaintext" in style


def _ascii_font_is_code(style: str) -> bool:
    return "mso-ascii-font-family" in style and any(font in style for font in CODE_FONTS)


def _classify_text(text: str, *, full: bool, ascii_code: bool) -> list[tuple[bool, str]]:
    if not text or _is_vml(text):
        return []
    if full:
        return [(True, text)]
    if not ascii_code:
        return [(False, text)]
    pieces: list[tuple[bool, str]] = []
    last = 0
    for match in ASCII_RUN.finditer(text):
        if match.start() > last:
            pieces.append((False, text[last : match.start()]))
        token = match.group(0)
        pieces.append((len(token) >= 2, token))
        last = match.end()
    if last < len(text):
        pieces.append((False, text[last:]))
    return pieces


def _is_vml(text: str) -> bool:
    folded = text.lower()
    return "v:shape" in folded or "vml" in folded or "shapetype" in folded


def _text_from_pieces(element: HtmlElement, pieces: list[tuple[bool, str]]) -> dict | None:
    plain = _clean("".join(text for _code, text in pieces))
    if not plain:
        return None
    total = sum(len(text.strip()) for _code, text in pieces)
    code_chars = sum(len(text.strip()) for code, text in pieces if code)
    ratio = code_chars / total if total else 0
    own = f"{element.get('class') or ''} {element.get('style') or ''}".lower()
    if ratio >= 0.75 or "msoplaintext" in own:
        return {"kind": "code", "text": plain}
    display = _inline_code(pieces)
    if display.startswith("- ") or display[:1] in "•·●○■▪►▶":
        return {"kind": "list", "text": f"- {display.lstrip('-•·●○■▪►▶ ').strip()}"}
    numbered = re.match(r"^(\d+)[.、]\s+(.+)", display)
    if numbered and len(numbered.group(2)) <= 80:
        return {"kind": "list", "text": f"{numbered.group(1)}. {numbered.group(2)}"}
    return {"kind": "p", "text": display}


def _inline_code(pieces: list[tuple[bool, str]]) -> str:
    chunks: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        if not buffer:
            return
        raw = "".join(buffer)
        buffer.clear()
        stripped = raw.strip().strip("`")
        if len(stripped) < 2 or re.fullmatch(r"\d+[.、]?", stripped):
            chunks.append(raw)
            return
        lead = raw[: len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()) :]
        chunks.append(f"{lead}`{stripped}`{trail}")

    for code, text in pieces:
        if code:
            buffer.append(text)
        else:
            flush()
            chunks.append(text)
    flush()
    return _clean("".join(chunks))


def _list(element: HtmlElement, *, ordered: bool) -> str:
    lines = []
    for index, item in enumerate(element.xpath("./li"), start=1):
        text = _clean("".join(item.itertext()))
        if not text:
            continue
        prefix = f"{index}." if ordered else "-"
        lines.append(f"{prefix} {text}")
    return "\n".join(lines)


def _table(element: HtmlElement) -> str:
    rows = []
    for tr in element.xpath("./thead/tr|./tbody/tr|./tr"):
        cells = [_clean("".join(cell.itertext())) for cell in tr.xpath("./th|./td")]
        if any(cells):
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    if (
        width == 2
        and len(rows) <= 2
        and all(len(row) < 2 or not row[0].strip() for row in rows)
    ):
        note = _clean(" ".join(row[1] for row in rows))
        if note:
            return "\n".join(f"> {line}" if line else ">" for line in note.splitlines())
        return ""
    padded = [row + [""] * (width - len(row)) for row in rows]
    def line(row: list[str]) -> str:
        escaped = [cell.replace("|", "\\|") for cell in row]
        return "| " + " | ".join(escaped) + " |"
    header = line(padded[0])
    rule = "| " + " | ".join("---" for _ in range(width)) + " |"
    body = "\n".join(line(row) for row in padded[1:])
    return "\n".join(part for part in (header, rule, body) if part)


def _copy_image(src: str, html_path: Path, image_dir: Path, index: int) -> str:
    if not src or src.startswith("data:"):
        return ""
    candidate = (html_path.parent / src).resolve()
    if not candidate.is_file():
        return ""
    if candidate.suffix.lower() not in IMAGE_EXT:
        return ""
    if candidate.stat().st_size < 80:
        return ""
    image_dir.mkdir(parents=True, exist_ok=True)
    name = f"c{index:03d}{candidate.suffix.lower()}"
    shutil.copyfile(candidate, image_dir / name)
    return f"img/{name}"


def _split_chapters(blocks: list[dict], fallback_title: str) -> list[dict]:
    chapters: list[dict] = []
    current: dict | None = None
    skipping = False
    saw_h1 = any(block["kind"] == "h" and block["level"] == 1 for block in blocks)
    if not saw_h1:
        return [{"title": fallback_title, "blocks": _demote(blocks)}]
    for block in blocks:
        if block["kind"] == "h" and block["level"] == 1:
            if is_contents_title(block["text"]):
                skipping = True
                current = None
                continue
            skipping = False
            current = {"title": block["text"], "blocks": []}
            chapters.append(current)
            continue
        if skipping or current is None:
            continue
        current["blocks"].append(block)
    if not chapters:
        return [{"title": fallback_title, "blocks": _demote(blocks)}]
    return chapters


def _demote(blocks: list[dict]) -> list[dict]:
    """Keep a topic that has no h1 from starting at markdown h1."""
    return blocks


def _blocks_to_markdown(blocks: list[dict]) -> str:
    pieces: list[str] = []
    code: list[str] = []
    lists: list[str] = []

    def flush_code() -> None:
        if not code:
            return
        pieces.append("```\n" + "\n".join(code).rstrip() + "\n```")
        code.clear()

    def flush_list() -> None:
        if not lists:
            return
        pieces.append("\n".join(lists))
        lists.clear()

    for block in blocks:
        kind = block["kind"]
        if kind == "code":
            flush_list()
            code.extend(block["text"].splitlines() or [""])
            continue
        flush_code()
        if kind == "list":
            lists.extend(block["text"].splitlines())
            continue
        flush_list()
        if kind == "h":
            hashes = max(2, min(6, block["level"]))
            pieces.append(f"{'#' * hashes} {block['text']}")
        elif kind == "image":
            pieces.append(f"![]({block['text']})")
        elif kind == "table":
            pieces.append(block["text"])
        elif block["text"]:
            pieces.append(block["text"])
    flush_code()
    flush_list()
    return re.sub(r"\n{3,}", "\n\n", "\n\n".join(pieces))
