from sorting_and_searching.bubble_sort import bubble_sort


def test_bubble_sort_when_sorted_then_numbers_are_arranged_correctly():
    numbers = [-2, 45, 0, 11, -9]
    expected = [-9, -2, 0, 11, 45]
    
    actual = bubble_sort(numbers)
    
    assert actual == expected
    