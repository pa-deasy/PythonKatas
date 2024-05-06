import pytest

from longest_substring_with_n_chars import longest_substring_of


def test_longest_substring_of_when_substring_of_2_then_as_expected():
    word = 'aaccbbaaaabcbcbcccccccccc'
    expected = 'bcbcbcccccccccc'
    
    actual = longest_substring_of(2, word)
    
    assert actual == expected
