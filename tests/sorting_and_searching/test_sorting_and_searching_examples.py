from sorting_and_searching.sorting_and_searching_examples import group_anagrams, search_rotated_array, sorted_merge


def test_sorted_merge_when_sorted_then_resulting_array_is_in_order():
    a = [3, 4, 8, 12, 17, 20, 91, None, None, None, None]
    b = [1, 5, 9, 54]
    expected = [1, 3, 4, 5, 8, 9, 12, 17, 20, 54, 91]
    
    actual = sorted_merge(a, b)
    
    assert actual == expected
    
    
def test_group_anagrams_when_sorted_then_resulting_array_is_in_order():
    input = ['evil', 'poor', 'kinder', 'ropo', 'poop', 'vile', 'renkid']
    expected = ['kinder', 'renkid', 'evil', 'vile', 'poop', 'poor', 'ropo']
    
    actual = group_anagrams(input)
    
    assert actual == expected
    
    
def test_search_rotated_when_element_found_then_returns_index():
    index = search_rotated_array(numbers=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=5)
    
    assert index == 8
    
    
def test_search_rotated_when_repeatative_elements_found_then_returns_index():
    index = search_rotated_array(numbers=[1, 1, 1, 1, 1, 2, 1, 1, 1, 1], target=2)
    
    assert index == 5
    