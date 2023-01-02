import pytest

from longest_increasing_subsequence import longest_increasing_subsequence_from


@pytest.mark.parametrize(
    "numbers,expected",
    [
        pytest.param([3, 10, 2, 1, 20], 3),
        pytest.param([3, 2], 1),
        pytest.param([50, 3, 10, 7, 40, 80], 4),
        pytest.param([9, 10, 2, 3, 5, 6, 7, 8, 20], 7),
    ]
)
def test_longest_increasing_subsequence_from_when_varying_sets_then_as_expected(numbers, expected):
    actual = longest_increasing_subsequence_from(numbers)
    
    assert actual == expected
    