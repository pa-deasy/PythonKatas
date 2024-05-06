import pytest

from selection_sort import selection_sort


def test_selection_sort_when_unordered_then_ordered_as_expected():
    expected = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    numbers = [5, 2, 1, 7, 4, 8, 3, 6, 9]
    
    actual = selection_sort(numbers)
    
    assert actual == expected