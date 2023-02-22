import pytest

from all_paths_maze import Direction, all_possible_paths

@pytest.fixture
def single_path_maze():
    return [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0], 
        [0, 1, 1, 1]
    ]
    
@pytest.fixture
def two_path_maze():
    return [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0], 
        [0, 1, 1, 1]
    ]
    

def test_all_possible_paths_when_one_path_exists_then_returned(single_path_maze):
    paths = all_possible_paths(single_path_maze)
    
    assert len(paths) == 1
    only_path = paths[0]
    assert only_path[0] == Direction.DOWN
    assert only_path[1] == Direction.RIGHT
    assert only_path[2] == Direction.DOWN
    assert only_path[3] == Direction.DOWN
    assert only_path[4] == Direction.RIGHT
    assert only_path[5] == Direction.RIGHT
    

def test_all_possible_paths_when_two_paths_exist_then_two_returned(two_path_maze):
    paths = all_possible_paths(two_path_maze)
    
    assert len(paths) == 2
    
    first_path = paths[0]
    assert first_path[0] == Direction.DOWN
    assert first_path[1] == Direction.DOWN
    assert first_path[2] == Direction.RIGHT
    assert first_path[3] == Direction.DOWN
    assert first_path[4] == Direction.RIGHT
    assert first_path[5] == Direction.RIGHT
    
    second_path = paths[1]
    assert second_path[0] == Direction.DOWN
    assert second_path[1] == Direction.RIGHT
    assert second_path[2] == Direction.DOWN
    assert second_path[3] == Direction.DOWN
    assert second_path[4] == Direction.RIGHT
    assert second_path[5] == Direction.RIGHT
