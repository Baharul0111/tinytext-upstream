"""Regression test for a known, unfixed bug — see the truncate() issue.

Marked xfail(strict=True) so CI stays green while the bug is open. Fixing
`truncate()` will make this pass, which turns the strict marker itself into a
failure — remove the marker in the same pull request.
"""

import pytest

from tinytext import truncate


def test_truncate_never_exceeds_limit():
    result = truncate("hello world", 8)
    assert len(result) <= 8
