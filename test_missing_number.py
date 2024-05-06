import pytest

from missing_number import get_missing_number


def test_get_missing_number_when_exists_then_returned():
    numbers = [1, 2, 4, 6, 3, 7, 8]
    
    missing_number = get_missing_number(numbers)
    
    assert missing_number == 5
