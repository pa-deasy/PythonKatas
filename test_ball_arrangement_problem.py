import pytest

from ball_arrangement_problem import possible_arrangements



@pytest.mark.parametrize(
    "reds,greens,blues,expected",
    [
        pytest.param(1, 1, 0, 2),
        pytest.param(1, 1, 1, 6),
        pytest.param(2, 1, 1, 6),
    ]
)
def test_possible_arrangements_when_predicted_then_as_expected(reds, greens, blues, expected):
    actual = possible_arrangements(reds, greens, blues)
    
    assert actual == expected
    
# (1, 1, 0, 2)
#  r g | g r

# (1, 1, 1, 6)
#  r g b | g r b | b r g | b g r | g b r | r b g

