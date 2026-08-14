"""The suite a contributor is expected to keep green."""

from tinytext import slugify, truncate, word_count, word_wrap


def test_slugify_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_collapses_runs():
    assert slugify("a --- b") == "a-b"


def test_truncate_leaves_short_text_alone():
    assert truncate("hello", 20) == "hello"


def test_truncate_appends_ellipsis():
    assert truncate("hello world", 8).endswith("...")


def test_truncate_zero_limit():
    assert truncate("hello", 0) == ""


def test_word_count():
    assert word_count("one two  three") == 3


def test_word_count_empty():
    assert word_count("") == 0


def test_word_wrap_basic():
    assert word_wrap("the quick brown fox", 10) == ["the quick", "brown fox"]


def test_word_wrap_short_text_is_one_line():
    assert word_wrap("hello", 10) == ["hello"]


def test_slugify_unicode():
    assert slugify("café") == "cafe"
    assert slugify("Héllo Wörld") == "hello-world"


def test_slugify_non_ascii_returns_empty():
    assert slugify("日本語") == ""
