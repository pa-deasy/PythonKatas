import pytest

from time_in_words import time_in_words


@pytest.mark.parametrize(
    "hour,minute,expected",
    [
        pytest.param(5, 0, "five o' clock"),
        pytest.param(5, 1, "one minute past five"),
        pytest.param(5, 10, "ten minutes past five"),
        pytest.param(5, 30, "half past five"),
        pytest.param(5, 40, "twenty minutes to six"),
        pytest.param(5, 45, "quarter to six"),
        pytest.param(5, 47, "thirteen minutes to six"),
        pytest.param(5, 28, "twenty eight minutes past five")
    ]
)
def test_time_in_words_when_converted_then_as_expected(hour, minute, expected):
    actual = time_in_words(hour, minute)
    
    assert actual == expected
