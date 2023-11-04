from recursion_and_dynamic.recursion_and_dynamic_examples import RobotGrid, count_ways, fibonacci, find_magic_index, find_magic_index_with_duplicates


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