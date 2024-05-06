import pytest

from sorting import quicksort, mergesort


def test_quicksort_when_sorted_then_expected():
    numbers = [57, 2, 13, 3, 1, 81]
    expected = [1, 2, 3, 13, 57, 81]
    
    actual = quicksort(numbers)
    assert actual == expected


def test_mergesort_when_sorted_then_expected():
    numbers = [57, 2, 13, 3, 1, 81]
    expected = [1, 2, 3, 13, 57, 81]
    
    actual = mergesort(numbers)
    assert actual == expected
