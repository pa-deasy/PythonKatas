import pytest

from majority_element import get_majority_element


def test_get_majority_element_when_exists_then_returned():
    numbers = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    
    majority_element = get_majority_element(numbers)
    
    assert majority_element == 4
    
    
def test_get_majority_element_when_none_exists_then_none_returned():
    numbers = [3, 3, 4, 2, 4, 4, 2, 4]
    
    majority_element = get_majority_element(numbers)
    
    assert majority_element is None
