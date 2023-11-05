from typing import Set
from recursion_and_dynamic.recursion_and_dynamic_examples import RobotGrid, Tower, all_subsets_of, count_ways, fibonacci, find_magic_index, find_magic_index_with_duplicates, recurse_multiply_efficient, recursive_multiply


def test_fibonacci_when_calculated_then_result_is_as_expected():
    fib = fibonacci(8)
    
    assert fib == 21
    

def test_count_ways_when_calculated_then_number_of_possible_ways_is_correct():
    assert count_ways(6) == 24
    
    
def test_robot_grid_when_path_possible_then_is_returned():
    grid = RobotGrid()
    
    path = grid.get_path()
    
    assert len(path) == 7
    
    
def test_find_magic_index_when_one_exists_then_returns_index():
    numbers = [-2, -1, 0, 1, 4, 10, 17, 20]
    
    magic_index = find_magic_index(numbers, 0, len(numbers) - 1)
    
    assert magic_index == 4
    
    
def test_find_magic_index_when_one_exists_and_all_elements_are_searched_then_returns_index():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 7]
    
    magic_index = find_magic_index(numbers, 0, len(numbers) - 1)
    
    assert magic_index == 7
    
    
def test_find_magic_index_with_duplicates_when_one_exists_then_returns_index():
    numbers = [-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13]
    
    magic_index = find_magic_index_with_duplicates(numbers, 0, len(numbers) - 1)
    
    assert magic_index == 2
    
    
def test_all_subsets_of_when_empty_set_then_returns_expected_list_of_subsets():
    expected = [[]]
    
    subsets = all_subsets_of([])
    
    assert subsets == expected
    

def test_all_subsets_of_when_singe_num_in_set_then_returns_expected_list_of_subsets():
    expected = [[], [9]]
    
    subsets = all_subsets_of([9])
    
    assert subsets == expected
    
    
def test_all_subsets_of_when_two_nums_in_set_then_returns_expected_list_of_subsets():
    expected = [[], [9], [1], [9, 1]]
    
    subsets = all_subsets_of([9, 1])
    
    assert subsets == expected
    
    
def test_all_subsets_of_when_three_nums_in_set_then_returns_expected_list_of_subsets():
    expected = [[], [9], [1], [9, 1], [5], [9, 5], [1, 5], [9, 1, 5]]
    
    subsets = all_subsets_of([9, 1, 5])
    
    assert subsets == expected

    
def test_recursive_multiply_when_multiplied_then_returns_expected_answer():
    assert recursive_multiply(4, 5) == 20
    

def test_recursive_multiply_efficient_when_multiplied_then_returns_expected_answer():
    assert recurse_multiply_efficient(7, 5) == 35
    
    
def test_hanoi_towers_when_disks_moved_to_last_tower_then_last_tower_ordered_as_expected():
    tower_a = Tower()
    tower_b = Tower()
    tower_c = Tower()
    
    tower_a.add(5)
    tower_a.add(4)
    tower_a.add(3)
    tower_a.add(2)
    tower_a.add(1)
    
    tower_a.move_disks(5, tower_c, tower_b)
    
    assert tower_a.disks.is_empty() is True
    assert tower_b.disks.is_empty() is True
    assert tower_c.disks.peek() == 1