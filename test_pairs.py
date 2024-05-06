import pytest

from pairs import pairs_with_diff_summing_to


@pytest.mark.parametrize(
    "target,numbers,expected",
    [
        pytest.param(1, [1, 2, 3, 4], 3),
        pytest.param(2, [1, 5, 3, 4, 2], 3)
    ]
)
def test_pairs_with_diff_summing_to_when_pairs_exist_then_returns_pairs(target, numbers, expected):
    actual = pairs_with_diff_summing_to(target, numbers)
    
    assert actual == expected
