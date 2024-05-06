import pytest

from calculator import add


def test_add_when_all_positive_then_expected_sum():
    numbers = [3, 8, 10, 24]
    
    actual = add(0, numbers)
    
    assert actual == 45
    
    
def test_add_when_negative_and_positive_then_expected_sum():
    numbers = [3, 8, -2, 24]
    
    actual = add(0, numbers)
    
    assert actual == 33
