import pytest
from sorting_and_searching.sorting_and_searching_examples import DataStream, Listy, check_duplicates, group_anagrams, search_matrix, search_rotated_array, search_sorted_matrix, sort_to_alternating, sorted_merge, sparse_search


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
    
    
def test_index_of_listy_when_target_exists_then_correct_index_returned():
    listy = Listy([4, 3, 14, 1, 9, 7])  #[1, 3, 4, 7, 9, 14]
    
    index = listy.index_of(7)
    
    assert index == 3
    
    
def test_binary_search_when_element_exists_return_index():
    listy = Listy([1, 2, 3, 4, 5, 6, 7])
    
    index = listy.binary_search(4, 0, 6)
    
    assert index == 3
    
    
def test_binary_search_when_element_does_not_exist_return_none():
    listy = Listy([1, 2, 3, 4, 5, 6, 7])
    
    index = listy.binary_search(9, 0, 6)
    
    assert index is None
    
    
def test_sparse_search_when_word_exists_then_index_is_returned():
    words = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
    
    index = sparse_search(words, 'ball')
    
    assert index == 4
    
    
def test_sparse_search_when_word_does_not_exist_then_none_is_returned():
    words = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
    
    index = sparse_search(words, 'patrick')
    
    assert index is None
    
    
def test_check_duplicates_when_duplicates_exists_then_are_printed():
    numbers = [34, 32, 80, 29, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 283, 833, 554, 1002, 1034, 1932, 2038, 29001, 28833, 27833, 30939, 3, 31383]
    
    duplicates = check_duplicates(numbers)
    
    assert duplicates == [3]
    
    
@pytest.fixture
def sorted_matrix():
    return [
        [15, 20, 40, 85],
        [20, 35, 80, 95],
        [30, 55, 95, 105],
        [40, 80, 100, 120]
    ]
    
    
def test_search_sorted_matrix_when_target_exists_then_matrix_position_returned(sorted_matrix):
    matrix_position = search_sorted_matrix(sorted_matrix, 55)
    
    assert matrix_position.column == 1
    assert matrix_position.row == 2
    

def test_search_sorted_matrix_when_target__does_not_exist_then_none_returned(sorted_matrix):
    matrix_position = search_sorted_matrix(sorted_matrix, 57)
    
    assert matrix_position is None
    
    
@pytest.fixture
def matrix():
    return [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    
def test_search_matrix_when_target_exists_then_matrix_position_returned(matrix):
    matrix_position = search_matrix(matrix, 14)
    
    assert matrix_position.row == 2
    assert matrix_position.column == 3
    

def test_search_matrix_when_target_does_not_exist_then_none_returned(matrix):
    matrix_position = search_matrix(matrix, 309)
    
    assert matrix_position is None
    

def test_stream_when_multiple_elements_tracked_then_arranges_tree_in_sorted_order():
    stream = DataStream()
    
    stream.track(20)
    stream.track(15)
    stream.track(10)
    stream.track(5)
    stream.track(13)
    stream.track(25)
    stream.track(23)
    stream.track(24)
    
    assert stream.root_rank_node.data == 20
    assert stream.root_rank_node.left.data == 15
    assert stream.root_rank_node.left.left.data == 10
    assert stream.root_rank_node.left.left.left.data == 5
    assert stream.root_rank_node.left.left.right.data == 13
    assert stream.root_rank_node.right.data == 25
    assert stream.root_rank_node.right.left.data == 23
    assert stream.root_rank_node.right.left.right.data == 24
    
    
def test_stream_when_rank_obtained_for_existing_element_then_rank_is_correct_count():
    stream = DataStream()
    stream.track(20)
    stream.track(15)
    stream.track(10)
    stream.track(5)
    stream.track(13)
    stream.track(25)
    stream.track(23)
    stream.track(24)
    
    assert stream.get_rank_of(24) == 6
    assert stream.get_rank_of(10) == 1
    assert stream.get_rank_of(15) == 3
    
    
def test_stream_when_rank_obtained_for_non_existing_element_then_rank_is_negative_one():
    stream = DataStream()
    stream.track(20)
    stream.track(15)
    stream.track(10)
    stream.track(5)
    stream.track(13)
    stream.track(25)
    stream.track(23)
    stream.track(24)
    
    assert stream.get_rank_of(1) == -1
    assert stream.get_rank_of(17) == -1
    assert stream.get_rank_of(55) == -1


def test_sort_to_alternating_when_sorted_then_alternating_peaks_and_valleys_returned():
    heights = [5, 3, 1, 2, 3] 
    expected = [3, 5, 1, 2, 3]
    
    actual = sort_to_alternating(heights)
    
    assert actual == expected