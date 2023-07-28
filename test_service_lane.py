import pytest

from service_lane import get_maximum_width_of_vehicles

@pytest.mark.parametrize(
    "widths,access_points,expected",
    [
        pytest.param(
            [2, 3, 2, 1], 
            [[1, 2], [2, 4]], 
            [2, 1]),
        pytest.param(
            [2, 3, 1, 2, 3, 2, 3, 3], 
            [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]], 
            [1, 2, 3, 2, 1]),
    ]
)
def test_get_maximum_width_of_vehicles_when_calculated_then_width_as_expected(widths, access_points, expected):
    actual = get_maximum_width_of_vehicles(widths, access_points)
    
    assert actual == expected