import pytest

from binary_search import binary_search_index


@pytest.mark.parametrize(
    "search_number,expected_index",
    [
        pytest.param(1, 0),
        pytest.param(2, 1),
        pytest.param(3, 2),
        pytest.param(4, 3),
        pytest.param(5, 4),
        pytest.param(6, 5),
        pytest.param(7, 6),
        pytest.param(8, 7),
        pytest.param(9, 8),
    ]
)
def test_binary_search_index_when_exists_then_index_returned(search_number, expected_index):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    actual = binary_search_index(search_number, numbers)
    
    assert actual == expected_index
    
    
def test_binary_search_index_when_not_exists_then_none_returned():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    actual = binary_search_index(11, numbers)
    
    assert actual is None