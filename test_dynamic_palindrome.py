import pytest

from dynamic_palindrome import longest_palindrome


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param('forgeeksskeegfor', 'geeksskeeg'),
        pytest.param('Geeks', 'ee'),
        pytest.param('dadcff', 'dad')
    ]
)
def test_longest_palindrome_when_exists_then_returns_longest(word, expected):
    longest = longest_palindrome(word)
    
    assert longest == expected
