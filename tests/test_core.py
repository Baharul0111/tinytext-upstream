"""The suite a contributor is expected to keep green."""

from tinytext import slugify, truncate, word_count


def test_slugify_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_collapses_runs():
    assert slugify("a --- b") == "a-b"


def test_truncate_leaves_short_text_alone():
    assert truncate("hello", 20) == "hello"


def test_truncate_appends_ellipsis():
    assert truncate("hello world", 8).endswith("...")
    assert len(truncate("hello world", 8)) == 8


def test_truncate_small_limit():
    assert len(truncate("hello", 2)) <= 2


def test_truncate_zero_limit():
    assert truncate("hello", 0) == ""


def test_word_count():
    assert word_count("one two  three") == 3


def test_word_count_empty():
    assert word_count("") == 0
