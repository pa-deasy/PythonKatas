import pytest

from manasa_and_stones import predict_values_of_last_stone


@pytest.mark.parametrize(
    "stones_count,stone_diff_a,stone_diff_b,expected",
    [
        pytest.param(3, 1, 2, [2, 3, 4]),
        pytest.param(4, 10, 100, [30, 120, 210, 300]),
    ]
)
def test_predict_values_of_last_stone_when_calculated_then_as_expected(stones_count, stone_diff_a, stone_diff_b, expected):
    actual = predict_values_of_last_stone(stones_count, stone_diff_a, stone_diff_b)
    
    assert actual == expected