import pytest

from string_comparison import longest_common_substring, longest_common_sequence


@pytest.mark.parametrize(
    "first_word,second_word,expected",
    [
        pytest.param('hish', 'fish', 3),
        pytest.param('hish', 'vista', 2),
    ]
)
def test_longest_common_substring_when_compared_then_as_expected(first_word, second_word, expected):
    actual = longest_common_substring(first_word, second_word)
    
    assert actual == expected
    

@pytest.mark.parametrize(
    "first_word,second_word,expected",
    [
        pytest.param('fosh', 'fish', 3),
        pytest.param('fosh', 'fort', 2)
    ]
)
def test_longest_common_sequence_when_compared_then_as_expected(first_word, second_word, expected):
    actual = longest_common_sequence(first_word, second_word)
    
    assert actual == expected
    