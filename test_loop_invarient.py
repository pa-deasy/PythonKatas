from loop_invarient import insertion_sort


def test_insertion_sort_when_sorted_then_expected_order():
    expected = [2, 3, 4, 5, 6, 7]
    
    actual = insertion_sort([7, 4, 3, 5, 6, 2])
    
    assert actual == expected