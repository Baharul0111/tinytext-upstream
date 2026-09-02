"""Core text helpers."""

from __future__ import annotations

import re
import unicodedata

_NON_WORD = re.compile(r"[^a-z0-9]+")

ELLIPSIS = "..."


def slugify(text: str) -> str:
    """Turn arbitrary text into a lowercase, hyphen-separated slug.

    Accented letters are transliterated to their ASCII base (e.g. é -> e).
    Characters with no ASCII equivalent are dropped; the function never raises.

    >>> slugify("Hello, World!")
    'hello-world'
    >>> slugify("Héllo Wörld")
    'hello-world'
    """
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
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
    return text[:limit] + ELLIPSIS


def word_count(text: str) -> int:
    """Count whitespace-separated words.

    >>> word_count("one two  three")
    3
    """
    return len(text.split())


def word_wrap(text: str, width: int) -> list[str]:
    """Break `text` into lines of at most `width` characters.

    Words are never split, so a single word longer than `width` gets a line to
    itself. Runs of whitespace collapse to one space.

    >>> word_wrap("the quick brown fox", 10)
    ['the quick', 'brown fox']
    """
    if width <= 0:
        return []
    lines: list[str] = []
    current = ""
    for word in text.split():
        if not current:
            current = word
        elif len(current) + 1 + len(word) > width:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}"
    if current:
        lines.append(current)
    return lines
