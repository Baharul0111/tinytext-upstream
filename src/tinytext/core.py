"""Core text helpers."""

from __future__ import annotations

import re

_NON_WORD = re.compile(r"[^a-z0-9]+")

ELLIPSIS = "..."


def slugify(text: str) -> str:
    """Turn arbitrary text into a lowercase, hyphen-separated slug.

    >>> slugify("Hello, World!")
    'hello-world'
    """
    return _NON_WORD.sub("-", text.lower()).strip("-")


def truncate(text: str, limit: int) -> str:
    """Shorten `text` so the result is at most `limit` characters.

    If the text is longer than `limit`, it is cut and an ellipsis is appended.

    >>> truncate("hello world", 8)
    'hello...'
    """
    if limit <= 0:
        return ""
    if len(text) <= limit:
        return text
    if limit < len(ELLIPSIS):
        return text[:limit]
    return text[:limit - len(ELLIPSIS)] + ELLIPSIS


def word_count(text: str) -> int:
    """Count whitespace-separated words.

    >>> word_count("one two  three")
    3
    """
    return len(text.split())
