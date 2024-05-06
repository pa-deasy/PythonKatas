import pytest
from typing import Set
from recursion_and_dynamic.recursion_and_dynamic_examples import Box, Canvas, Point, RobotGrid, Tower, all_permutations, all_permutations_with_dups, all_subsets_of, calculate_highest_stack, count_eval, count_ways, fibonacci, find_magic_index, find_magic_index_with_duplicates, parens_permutations, permutations_of_cents, permutations_of_queens, recurse_multiply_efficient, recursive_multiply


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
    

def test_all_permutations_when_permutations_generated_then_they_match_expected_list():
    word = 'bud'
    expected = ['bud', 'bdu', 'ubd', 'udb', 'dbu', 'dub']
    
    actual = all_permutations(word)
    
    assert actual == expected
    
    
def test_all_permutations_with_dups_when_permutations_generated_then_they_match_expected_list():
    word = 'buud'
    expected = ['buud', 'budu', 'bduu', 'ubud', 'ubdu', 'uubd', 'uudb', 'udbu', 'udub', 'dbuu', 'dubu', 'duub']
    
    actual = all_permutations_with_dups(word)
    
    assert actual == expected


def test_parens_permutations_when_generated_then_match_expected_list():
    expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
    
    actual = parens_permutations(3)
    
    assert actual == expected
    
    

@pytest.fixture
def blank_canvas():
    return Canvas(size=5)


@pytest.fixture
def part_red_canvas():
    canvas = Canvas(size=5)

    canvas.layout[0][0] = '#FF0000'
    canvas.layout[2][2] = '#FF0000'
    canvas.layout[3][3] = '#FF0000'
    canvas.layout[3][2] = '#FF0000'

    return canvas


def test_fill_with_color_when_blank_canvas_filled_with_green_then_all_canvas_is_green(blank_canvas):
    blank_canvas.fill_with_color('008000', Point(1, 1))

    assert blank_canvas.layout[0][0] == '008000'
    assert blank_canvas.layout[4][4] == '008000'


def test_fill_with_color_when_part_red_canvas_filled_with_green_then_select_parts_of_canvas_is_green(part_red_canvas):
    part_red_canvas.fill_with_color('008000', Point(3, 2))

    assert part_red_canvas.layout[0][0] == '#FF0000'
    assert part_red_canvas.layout[2][2] == '008000'
    assert part_red_canvas.layout[3][3] == '008000'
    assert part_red_canvas.layout[3][2] == '008000'


def test_permutations_of_cents_when_all_permutations_generated_then_match_expected_count():
    permutations = permutations_of_cents(25)

    assert len(permutations) == 13


def test_permutations_of_queens_when_all_permutations_generated_then_match_expected_count():
    permutations = permutations_of_queens()
    
    assert len(permutations) == 92
    
    
def test_calculate_highest_stack_when_calculated_then_returns_correct_height():
    box_1 = Box(width=7, height=7, dept=7)
    box_2 = Box(width=7, height=6, dept=7)
    box_3 = Box(width=5, height=3, dept=4)
    box_4 = Box(width=6, height=3, dept=8)
    box_5 = Box(width=2, height=1, dept=2)
    
    boxes = [box_4, box_1, box_3, box_2, box_5]
    
    height = calculate_highest_stack(boxes)
    
    assert height == 11
    
    
def test_count_eval():
    assert count_eval('1^0|0|1', False) == 2
    assert count_eval('0&0&0&1^1|0', True) == 10
