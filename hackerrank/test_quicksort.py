from quicksort import quicksort_numbers
import pytest


def test_quicksort_when_sorted_then_order_as_expected():
    expected = [1, 2, 3, 5, 7, 8, 9]
    
    actual = quicksort_numbers([1, 3, 9, 8, 2, 7, 5])
    
    assert actual == expected