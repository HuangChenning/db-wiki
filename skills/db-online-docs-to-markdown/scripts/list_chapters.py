#!/usr/bin/env python3
"""Print a book's chapter list as JSON.

Modes:
  oracle   docs.oracle.com toc.htm (skips toc, Next/Previous, other books)
  dameng   eco.dameng.com sidebar groups (first copy only)
  relative unique relative .html links, including site chrome
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urlparse

USER_AGENT = "Mozilla/5.0"
_HREF = re.compile(r"^(?:[A-Za-z0-9_+-]+/)*[A-Za-z0-9_+-]+\.html?$")
_SPACE = re.compile(r"\s+")
_PAGER = {"Next", "Previous"}


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8", "replace")


def parse_oracle(page: str, book_root: str) -> list[dict[str, str]]:
    root = book_root
    if root and not root.endswith("/"):
        root += "/"

    class Parser(HTMLParser):
        def __init__(self) -> None:
            super().__init__(convert_charrefs=True)
            self.chapters: list[dict[str, str]] = []
            self._seen: set[str] = set()
            self._parts: list[str] | None = None
            self._href: str | None = None

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag.lower() != "a" or self._parts is not None:
                return
            href = _local_href(dict(attrs).get("href") or "", root)
            if href is None or href in self._seen:
                return
            self._href = href
            self._parts = []

        def handle_endtag(self, tag: str) -> None:
            if tag.lower() != "a" or self._parts is None or self._href is None:
                return
            title = _SPACE.sub(" ", "".join(self._parts)).strip()
            href = self._href
            self._parts = None
            self._href = None
            if not title or title in _PAGER:
                return
            self._seen.add(href)
            self.chapters.append({"href": href, "title": title})

        def handle_data(self, data: str) -> None:
            if self._parts is not None:
                self._parts.append(data)

    parser = Parser()
    parser.feed(page)
    parser.close()
    return parser.chapters


def _local_href(href: str, book_root: str) -> str | None:
    href = href.split("#", 1)[0].split("?", 1)[0]
    if href.startswith("./"):
        href = href[2:]
    if book_root and href.startswith(book_root):
        href = href[len(book_root) :]
    elif href.startswith(("http://", "https://", "/")):
        return None
    if href in {"toc.htm", "toc.html"} or _HREF.fullmatch(href) is None:
        return None
    return href


def parse_dameng(page: str) -> list[dict[str, object]]:
    headers = list(re.finditer(r"font-weight:800;\">([^<]+)", page))
    books: list[dict[str, object]] = []
    seen_titles: set[str] = set()
    for index, match in enumerate(headers):
        title = _SPACE.sub(" ", html.unescape(match.group(1))).strip()
        if title in seen_titles:
            break
        seen_titles.add(title)
        end = headers[index + 1].start() if index + 1 < len(headers) else match.end()
        chunk = page[match.end() : end]
        chapters: list[dict[str, str]] = []
        seen: set[str] = set()
        for href, text in re.findall(r'href="([^"]+\.html)"[^>]*>([^<]+)', chunk):
            href = href.split("#", 1)[0]
            if href.startswith(("/", "http")) or href in seen:
                continue
            if _HREF.fullmatch(href) is None:
                continue
            seen.add(href)
            chapters.append({"href": href, "title": _SPACE.sub(" ", html.unescape(text)).strip()})
        books.append({"title": title, "chapters": chapters})
    return books


def parse_relative(page: str) -> list[dict[str, str]]:
    class Parser(HTMLParser):
        def __init__(self) -> None:
            super().__init__(convert_charrefs=True)
            self.chapters: list[dict[str, str]] = []
            self._seen: set[str] = set()
            self._parts: list[str] | None = None
            self._href: str | None = None

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag.lower() != "a" or self._parts is not None:
                return
            href = (dict(attrs).get("href") or "").split("#", 1)[0].split("?", 1)[0]
            if href.startswith("./"):
                href = href[2:]
            if href.startswith(("/", "http")) or _HREF.fullmatch(href) is None or href in self._seen:
                return
            self._href = href
            self._parts = []

        def handle_endtag(self, tag: str) -> None:
            if tag.lower() != "a" or self._parts is None or self._href is None:
                return
            title = _SPACE.sub(" ", "".join(self._parts)).strip()
            self._seen.add(self._href)
            self.chapters.append({"href": self._href, "title": title})
            self._parts = None
            self._href = None

        def handle_data(self, data: str) -> None:
            if self._parts is not None:
                self._parts.append(data)

    parser = Parser()
    parser.feed(page)
    parser.close()
    return parser.chapters


def main() -> None:
    parser = argparse.ArgumentParser(description="List chapters from a documentation HTML page")
    parser.add_argument("--mode", required=True, choices=("oracle", "dameng", "relative"))
    parser.add_argument("--url", required=True)
    parser.add_argument("--book-root", default="", help="Oracle book path prefix; default is the URL directory")
    parser.add_argument("--html", help="Read this local file instead of --url")
    args = parser.parse_args()
    page = open(args.html, encoding="utf-8").read() if args.html else fetch(args.url)
    if args.mode == "oracle":
        book_root = args.book_root or urlparse(args.url).path.rsplit("/", 1)[0] + "/"
        payload: object = parse_oracle(page, book_root)
    elif args.mode == "dameng":
        payload = parse_dameng(page)
    else:
        payload = parse_relative(page)
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
