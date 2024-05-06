import pytest

from circular_array_rotation import rotate_array


@pytest.mark.parametrize(
    "array,rotations,indexes,expected",
    [
        pytest.param([3, 4, 5], 11, [1, 2], [5, 3]),
        pytest.param(['a', 'b', 'c'], 2, [1, 2], ['c', 'a'])
    ]
)
def test_rotate_array_when_rotated_then_as_expected(array, rotations, indexes, expected):
    actual = rotate_array(array, rotations, indexes)
    
    assert actual == expected
    