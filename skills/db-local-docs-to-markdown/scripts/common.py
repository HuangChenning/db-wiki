"""Shared helpers for the local PDF/CHM manual converter."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
CONTENTS_TITLES = {"目录", "目次", "contents", "tableofcontents", "toc"}
PLACEHOLDER_SUMMARY = "待补。"

# Longer keys first. Used only to draft a slug; the agent confirms it.
SLUG_HINTS = (
    ("读写分离", "read-write-split"),
    ("数据守护概念", "data-watch"),
    ("数据守护", "data-watch-v2"),
    ("系统管理员", "administrator"),
    ("程序员", "programmer"),
    ("安全管理", "security"),
    ("作业系统", "job-system"),
    ("备份", "backup-restore"),
    ("集群代理", "cluster-agent"),
    ("技术支持", "support"),
    ("欢迎", "welcome"),
    ("前言", "preface"),
    ("dexp", "dexp-dimp"),
    ("dimp", "dexp-dimp"),
    ("dmpython", "dmpython"),
    ("dmdbchk", "dmdbchk"),
    ("dmfldr", "dmfldr"),
    ("dminit", "dminit"),
    ("dmlcvt", "dmlcvt"),
    ("disql", "disql"),
    ("proc", "proc"),
    ("sql", "sql-language"),
)


def display_name(name: str) -> str:
    """Recover a Chinese filename that macOS stored as Latin mojibake.

    Files that are already Unicode (they contain CJK) are returned unchanged.
    """
    normalized = unicodedata.normalize("NFC", name)
    if any("\u4e00" <= char <= "\u9fff" for char in normalized):
        return normalized
    for encoding in ("mac_roman", "cp1252", "latin1"):
        try:
            return normalized.encode(encoding).decode("gbk")
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
    return normalized


def norm_text(value: str) -> str:
    return re.sub(r"\s+", "", value).lower()


def is_contents_title(title: str) -> bool:
    return norm_text(title) in CONTENTS_TITLES


def book_key(title: str) -> str:
    text = norm_text(title)
    for suffix in ("使用手册", "操作手册", "手册", "帮助文档"):
        text = text.replace(suffix, "")
    text = re.sub(r"^dm\d+[_-]?", "", text)
    return text


def same_book(left: str, right: str) -> bool:
    if not left or not right:
        return False
    if left == right:
        return True
    longer, shorter = (left, right) if len(left) >= len(right) else (right, left)
    if longer.endswith(shorter) and longer[: -len(shorter)] in {"dm", "dm7", "dm8"}:
        return True
    return False


def suggest_slug(title: str) -> str:
    folded = title.lower()
    for hint, slug in SLUG_HINTS:
        if hint in folded or hint in title:
            return slug
    tokens = re.findall(r"[a-z][a-z0-9]*", folded)
    if tokens:
        return "-".join(tokens)[:40]
    return "book"


def suggest_group(title: str, fallback: str) -> str:
    if any(word in title for word in ("守护", "集群", "读写", "并行")):
        return "高可用与集群"
    if any(word in title.lower() for word in ("sql", "proc", "程序", "python", "disql")):
        return "SQL 与开发"
    if any(word in title for word in ("管理员", "安全", "备份", "作业")):
        return "管理"
    if any(word in title for word in ("前言", "欢迎", "技术支持", "说明")):
        return "说明"
    return fallback or "工具"


def default_stem(title: str, index: int) -> str:
    cleaned = re.sub(r"\s+", "", title)
    cleaned = re.sub(r'[\\/:*?"<>|#]+', "", cleaned).strip(".-")
    cleaned = cleaned[:40] or "chapter"
    return f"{index:02d}-{cleaned}"


def assign_stems(chapters: list[dict]) -> None:
    used: set[str] = set()
    for index, chapter in enumerate(chapters, start=1):
        stem = str(chapter.get("stem") or default_stem(str(chapter["title"]), index))
        stem = stem.strip()
        if stem in used:
            stem = f"{stem}-{index}"
        used.add(stem)
        chapter["stem"] = stem


def yaml_value(value: str) -> str:
    if value and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 ._()/-]*", value):
        return value
    return json.dumps(value, ensure_ascii=False)


def repo_relative(path: Path) -> str:
    resolved = path.resolve()
    for parent in (resolved.parent, *resolved.parents):
        if (parent / ".git").exists():
            try:
                return resolved.relative_to(parent).as_posix()
            except ValueError:
                break
    return resolved.as_posix()


def source_ref(path: Path, suffix: str = "") -> str:
    shown = repo_relative(path)
    return f"{shown}{suffix}" if suffix else shown


def load_manifest(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ("product", "version", "tags", "out", "books"):
        if key not in data:
            raise SystemExit(f"manifest missing {key}")
    out = Path(data["out"])
    if not str(out):
        raise SystemExit("manifest out is empty")
    if not isinstance(data["tags"], list) or not data["tags"]:
        raise SystemExit("tags must be a non-empty list")
    slugs: set[str] = set()
    for book in data["books"]:
        if book.get("skip"):
            continue
        slug = book.get("slug", "")
        if SLUG.fullmatch(slug) is None:
            raise SystemExit(f"bad slug {slug!r}")
        if slug in slugs:
            raise SystemExit(f"duplicate slug {slug}")
        slugs.add(slug)
        for key in ("title", "summary", "group", "kind", "source"):
            if not str(book.get(key, "")).strip():
                raise SystemExit(f"{slug} missing {key}")
        summary = str(book["summary"]).strip()
        if summary == PLACEHOLDER_SUMMARY or summary.startswith("待补"):
            raise SystemExit(f"{slug} summary is still a placeholder")
        if book["kind"] not in {"pdf", "chm"}:
            raise SystemExit(f"{slug} kind must be pdf or chm")
        if book["kind"] == "chm" and not str(book.get("topic", "")).strip():
            raise SystemExit(f"{slug} missing topic")
        source = Path(book["source"])
        if not source.is_file():
            raise SystemExit(f"{slug} source not found: {source}")
        chapters = book.get("chapters") or []
        if not isinstance(chapters, list):
            raise SystemExit(f"{slug} chapters must be a list")
        for chapter in chapters:
            if not str(chapter.get("title", "")).strip():
                raise SystemExit(f"{slug} has a chapter without a title")
    return data
