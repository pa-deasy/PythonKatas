from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


# 7.8 - Othello: Othello is played as follows: Each Othello piece is white on one side and black on the other.
# When a piece is surrounded by it's opponents on both the left and right sides, or both the top and bottom, it is said to be captured and its color is flipped.
# On your turn you must capture at least one of your opponents pieces. The game ends when either user has no more valid moves.
# The win is assigned to the person with the most pieces. Implement the object oriented design for Othello.
class Piece(Enum):
    BLACK = 'black'
    WHITE = 'white'


@dataclass
class Position:
    y: int
    x: int
    piece: Optional[Piece] = None
    

class Board:
    layout: List[List[Position]]
    is_finished: bool
    
    def __init__(self, size: int) -> None:
        self.is_finished = False
        self.layout = []
        for row_index in range(size):
            row: List[Position] = []
            for column_index in range(size):
                row.append(Position(y=row_index, x=column_index))
            self.layout.append(row)
            
    def get_position(self, y: int, x: int) -> Position:
        return self.layout[y][x]
    
    
    def set_piece_at_position(self, piece: Piece, y: int, x: int) -> None:
        self.layout[y][x].piece = piece
        
        
    def check_for_captures(self) -> None:
        return
    
    def get_black_white_count(self) -> (int, int):
        return
    

@dataclass
class Player:
    name: str
    piece: Piece
    score: int = 0
    
    
class Game:
    board: Board
    player1: Player
    player2: Player
    round_count: int
    
    def __init__(self, name1: str, name2: str) -> None:
        self.board = Board(8)
        self.player1 = Player(name=name1, piece=Piece.BLACK)
        self.player2 = Player(name=name2, piece=Piece.WHITE)
        self.round_count = 0
        self.is_won = False
        
        
    def play(self) -> None:
        while not self.board.is_finished:
            current_player = self.player2 if self.round_count % 2 == 0 else self.player1
            
            (y, x) = self.get_move()
            self.board.set_piece_at_position(current_player.piece, y, x)
            self.board.check_for_captures()
            (black_count, white_count) = self.board.get_black_white_count()
            self.player1.score = black_count
            self.player2.score = white_count
            
            self.round_count += 1
            
            
    def get_move(self) -> (int, int):
        return