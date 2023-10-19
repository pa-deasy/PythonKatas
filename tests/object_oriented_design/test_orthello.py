import pytest

from object_oriented_design.othello import Board, Piece


@pytest.fixture
def board():
    return Board(8)


def test_get_position_when_retrieved_then_as_expected(board):
    position = board.get_position(5, 3)
    
    assert position.y == 5
    assert position.x == 3
    assert position.piece is None
    

def test_set_piece_at_position_when_set_then_as_expected(board):
    board.set_piece_at_position(Piece.BLACK, 5, 3)
    position = board.get_position(5, 3)
    
    assert position.piece is Piece.BLACK