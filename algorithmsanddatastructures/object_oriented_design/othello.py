from enum import Enum
from typing import List, Optional, Tuple


# 7.8 - Othello: Othello is played as follows: Each Othello piece is white on one side and black on the other.
# When a piece is surrounded by it's opponents on both the left and right sides, or both the top and bottom, it is said to be captured and its color is flipped.
# On your turn you must capture at least one of your opponents pieces. The game ends when either user has no more valid moves.
# The win is assigned to the person with the most pieces. Implement the object oriented design for Othello.
class Piece(Enum):
    BLACK = 'black'
    WHITE = 'white'

    def get_opposite(self) -> 'Piece':
        if self == Piece.BLACK:
            return Piece.WHITE
        else:
            return Piece.BLACK 


class Board:
    size = 8
    layout: List[List[Optional[Piece]]]

    def __init__(self) -> None:
        self._setup_board()

    def _setup_board(self) -> None:
        columns = [None] * self.size
        self.layout = columns * self.size
        
        self.layout[3, 3] = Piece.BLACK
        self.layout[4, 4] = Piece.BLACK
        self.layout[3, 4] = Piece.WHITE
        self.layout[4, 3] = Piece.WHITE

    def is_valid_move(self, row: int, column: int) -> bool:
        return self._is_position_within_board(row, column) and self._is_position_empty(row, column)
    
    def _is_position_within_board(self, row: int, column: int) -> bool:
        return row >=0 and row < self.size and column >=0 and column < self.size
    
    def _is_position_empty(self, row: int, column: int) -> bool:
        return self.layout[row][column] == None
    
    def capture_position(self, row: int, column: int, piece: Piece) -> None:
        self.layout[row][column] = piece
        self._try_capture_left(row, column, piece)
        self._try_capture_right(row, column, piece)
        self._try_capture_above(row, column, piece)
        self._try_capture_below(row, column, piece)

    def _try_capture_left(self, row: int, column: int, piece: Piece) -> None:
        if not self._is_position_within_board(row, column - 2):
            return
        
        if self.layout[row][column - 2] == piece and self.layout[row][column - 1] == piece.get_opposite:
            self.layout[row][column - 1] = piece
            self._try_capture_left(row, column - 1, piece)

    def _try_capture_right(self, row: int, column: int, piece: Piece) -> None:
        if not self._is_position_within_board(row, column + 2):
            return
        
        if self.layout[row][column + 2] == piece and self.layout[row][column + 1] == piece.get_opposite:
            self.layout[row][column + 1] = piece
            self._try_capture_right(row, column + 1, piece)

    def _try_capture_above(self, row: int, column: int, piece: Piece) -> None:
        if not self._is_position_within_board(row - 2, column):
            return
        
        if self.layout[row - 2][column] == piece and self.layout[row - 1][column] == piece.get_opposite:
            self.layout[row - 1][column] = piece
            self._try_capture_above(row - 1, column, piece)

    def _try_capture_below(self, row: int, column: int, piece: Piece) -> None:
        if not self._is_position_within_board(row + 2, column):
            return
        
        if self.layout[row + 2][column] == piece and self.layout[row + 1][column] == piece.get_opposite:
            self.layout[row + 1][column] = piece
            self._try_capture_below(row + 1, column, piece)

    def is_board_full(self) -> bool:
        for row_index in range(self.size):
            for column_index in range(self.size):
                if self.layout[row_index][column_index] == None:
                    return False

        return True
    
    def get_pieces_count(self) -> Tuple[int, int]:
        black_count = 0
        white_count = 0
        for row_index in range(self.size):
            for column_index in range(self.size):
                if self.layout[row_index, column_index] == Piece.BLACK:
                    black_count += 1
                else:
                    white_count += 1

        return (black_count, white_count)


class Game:
    board: Board

    def __init__(self) -> None:
        self.board = Board()

    def start(self) -> None:
        turn = Piece.BLACK
        while not self.board.is_board_full():
            row, column = self._get_player_input(turn)
            if not self.board.is_valid_move(row, column):
                print('Invalid move')
                continue
            
            self.board.capture_position(row, column, turn)
            turn = turn.get_opposite()

        black_count, white_count = self.board.get_pieces_count()
        winner = black_count if black_count > white_count else white_count
        print(f'The winner is {winner}. Black count: {black_count} vs White count: {white_count}')

    
    def _get_player_input(self, piece: Piece) -> Tuple[int, int]:
        ...
