import pytest

from simple_search import simple_search_index


def test_simple_search_index_when_exists_then_index_returned():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    actual = simple_search_index(5, numbers)
    
    assert actual == 4
    
    
def test_simple_search_index_when_not_exists_then_none_returned():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    actual = simple_search_index(11, numbers)
    
    assert actual is None