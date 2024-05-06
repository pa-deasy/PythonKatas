import pytest

from index_search import index_search

@pytest.mark.parametrize(
    "numbers,target,expected",
    [
        pytest.param([1, 2, 3], 3, 2),
        pytest.param([1, 4, 5, 7, 9, 12], 4, 1),
        pytest.param([1, 2, 3], 9, -1),
    ]
)
def test_index_search_when_searched_then_expected_index_returned(numbers, target, expected):
    actual = index_search(numbers, target)
    
    assert actual == expected