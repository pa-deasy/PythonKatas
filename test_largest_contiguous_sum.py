import pytest

from largest_contiguous_sum import largest_contiguous_sum_of


@pytest.mark.parametrize(
    "numbers,expected",
    [
        pytest.param([-2, -3, 4, -1, -2, 1, 5, -3], 7),
        pytest.param([1, 2, 3, -2, 5], 9),
        pytest.param([ -1, -2, -3, -4], -1),
    ]
)
def test_largest_contiguous_sum_of_when_varying_sets_then_as_expected(numbers, expected):
    actual = largest_contiguous_sum_of(numbers)
    
    assert actual == expected
