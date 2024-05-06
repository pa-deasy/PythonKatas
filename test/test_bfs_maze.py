import pytest

from bfs_maze import Position, quickest_path


@pytest.fixture
def maze():
    maze: list[list[int]] = []
    maze.append([1, 0, 1, 1, 1, 1, 0, 1, 1, 1])
    maze.append([1, 0, 1, 0, 1, 1, 1, 0, 1, 1])
    maze.append([1, 1, 1, 0, 1, 1, 1, 1, 1, 1])
    maze.append([1, 0, 0, 0, 1, 0, 0, 0, 1, 1])
    maze.append([1, 1, 1, 0, 1, 1, 1, 0, 1, 0])
    maze.append([1, 0, 1, 1, 1, 1, 0, 1, 1, 0])
    maze.append([1, 0, 0, 0, 0, 0, 0, 0, 1, 1])
    maze.append([1, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    maze.append([1, 0, 0, 0, 0, 1, 0, 1, 1, 1])
    maze.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    return maze


@pytest.fixture
def impossible_maze():
    maze: list[list[int]] = []
    maze.append([1, 0, 1, 1, 1, 1, 0, 1, 1, 1])
    maze.append([1, 0, 1, 0, 1, 1, 1, 0, 1, 1])
    maze.append([1, 1, 1, 0, 1, 1, 1, 1, 1, 1])
    maze.append([1, 0, 0, 0, 1, 0, 0, 0, 1, 1])
    maze.append([1, 1, 1, 0, 1, 1, 1, 0, 1, 0])
    maze.append([1, 0, 1, 1, 1, 1, 0, 1, 1, 0])
    maze.append([1, 0, 0, 0, 0, 0, 0, 0, 1, 1])
    maze.append([1, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    maze.append([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
    maze.append([1, 1, 1, 1, 1, 1, 1, 1, 0, 1])
    return maze
    

def test_quickest_path_when_numberous_paths_then_returns_fastest(maze):
    step_count = quickest_path(maze)
    
    assert step_count == 18
    

def test_quickest_path_when_no_paths_then_returns_zero(impossible_maze):
    step_count = quickest_path(impossible_maze)
    
    assert step_count == 0
    

def test_position_matches_when_matches_then_true():
    position = Position(x=1, y=1, steps_traveled=0)
    assert position.matches(Position(1,1, steps_traveled=0)) is True
    

def test_position_matches_when_not_matches_then_false():
    position = Position(x=1, y=1, steps_traveled=0)
    assert position.matches(Position(1,2, steps_traveled=0)) is False
    

def test_postion_is_within_maze_when_it_is_then_true():
    position = Position(x=1, y=1, steps_traveled=0)
    assert position.is_within_maze(9) is True
    

def test_postion_is_within_maze_when_is_not_then_false():
    position = Position(x=10, y=-1, steps_traveled=0)
    assert position.is_within_maze(9) is False
    

def test_postion_surrounding_positions_when_all_on_board_then_returned():
    position = Position(x=2, y=2, steps_traveled=0)
    surrounding_positions =  position.surrounding_positions(9)
    
    assert len(surrounding_positions) == 4
    

def test_postion_surrounding_positions_when_some_on_board_then_returned():
    position = Position(x=0, y=0, steps_traveled=0)
    surrounding_positions =  position.surrounding_positions(9)
    
    assert len(surrounding_positions) == 2
