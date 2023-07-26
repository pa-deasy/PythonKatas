import pytest

from minimum_distances import minimum_distance

@pytest.mark.parametrize(
    "numbers, expected",
    [
        pytest.param([3, 2, 1, 2, 3], 2),
        pytest.param([7, 1, 3, 4, 1, 7], 3),
        pytest.param([1, 2, 3, 4], -1),
    ]
)
def test_minimum_distance_when_calculatated_then_as_expected(numbers, expected):
    actual = minimum_distance(numbers)
    
    assert actual == expected
