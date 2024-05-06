import pytest

from cavity_map import mark_cavities

@pytest.mark.parametrize(
    "grid,expected",
    [
        pytest.param(['989', '191', '111'], ['989', '1X1', '111']),
        pytest.param(['1112', '1912', '1892', '1234'], ['1112', '1X12', '18X2', '1234']),
    ]
)
def test_mark_cavities_when_marked_then_cavities_as_expected(grid, expected):
    actual = mark_cavities(grid)
    
    assert actual == expected
