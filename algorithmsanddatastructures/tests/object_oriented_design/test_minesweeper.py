import pytest

from object_oriented_design.minesweeper import Board, Cell, CellValue, Position


@pytest.fixture
def board():
    return Board()


def test_get_cell_at_position_when_retrieved_then_matches_expected_cell(board):
    position = Position(3, 2)
    
    cell = board.get_cell_at_position(position)
    
    assert cell.position.is_equal_to(position) is True
    assert cell.value == CellValue.MINE
    
    
def test_position_is_on_board_when_is_on_board_then_returns_true(board):
    assert board.position_is_on_board(Position(3, 2)) is True
    assert board.position_is_on_board(Position(0, 0)) is True
    assert board.position_is_on_board(Position(6, 6)) is True
    

def test_position_is_on_board_when_not_on_board_then_returns_false(board):
    assert board.position_is_on_board(Position(-1, 2)) is False
    assert board.position_is_on_board(Position(2, -1)) is False
    assert board.position_is_on_board(Position(7, 6)) is False
    assert board.position_is_on_board(Position(6, 7)) is False
    
    
def test_is_empty_or_number_when_checked_returns_correct_bool():
    position = Position(3, 2)
    assert Cell(position=position, value=CellValue.MINE).is_empty_or_number() is False
    assert Cell(position=position, value=CellValue.EMPTY).is_empty_or_number() is True
    assert Cell(position=position, value=CellValue.THREEMINE).is_empty_or_number() is True
    
    
def test_uncover_position_when_mine_then_cell_is_marked_as_exposed_and_mine_triggered_is_true(board):
    position = Position(3, 2)
    
    board.uncover_position(position)
    
    assert board.get_cell_at_position(position).exposed is True
    assert board.mine_triggered is True
    
    
def test_uncover_position_when_empty_cell_then_uncovers_adjacent_cells(board):
    position = Position(1, 0)
    expected_exposed = [
        Position(0, 0), Position(0, 1),
        Position(1, 0), Position(1, 1),
        Position(2, 0), Position(2, 1),
        Position(3, 0), Position(3, 1),
        Position(4, 0), Position(4, 1), Position(4, 2), Position(4, 3),
        Position(5, 0), Position(5, 1), Position(5, 2), Position(5, 3),
        Position(6, 0), Position(6, 1), Position(6, 2), Position(6, 3),
        ]
    
    expected_not_exposed = [
        Position(0, 2),
        Position(1, 2),
        Position(2, 2),
        Position(3, 2), Position(3, 3), Position(3, 4),
        Position(4, 4),
        Position(5, 4),
        Position(6, 4),
        ]
    
    board.uncover_position(position)
    assert board.cells_till_victory == 26
    
    for p in expected_exposed:
        assert board.get_cell_at_position(p).exposed is True
        
    for p in expected_not_exposed:
        assert board.get_cell_at_position(p).exposed is False
    