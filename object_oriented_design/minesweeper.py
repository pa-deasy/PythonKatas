from dataclasses import dataclass
from enum import IntEnum
from typing import List


# 7.10: Minesweeper: Design and implement a text-based Minesweeper game. Minesweeper is the classic single-player computer game where an N x N grid has B mines hidden
# across the grid. The remaining cells are either blank or have a number behind them. The numbers reflect the number of mines in the surrounding eight cells.
# The user then uncovers a cell, if it is a bomb, the player loses. If it is a number, the number is exposed. 
# If it is a blank cell, this cell and adjacent blank cells(up to and including the surrounding numberic cells) are exposed.
# The player wins when all non-mine cells are exposed. The player can also flag certain places as potential mines. This doesn't affect gameplay, other
# than to block a player from accidentally selecting a cell that is thought to have a mine.
class Position:
    y: int
    x: int
    
    def __init__(self, y: int, x: int) -> None:
        self.y = y
        self.x = x
    
    def is_equal_to(self, other: 'Position') -> bool:
        return self.y == other.y and self.x == other.x
    
    def above(self) -> 'Position':
        return Position(self.y - 1, self.x)
    
    def below(self) -> 'Position':
        return Position(self.y + 1, self.x)
    
    def left(self) -> 'Position':
        return Position(self.y, self.x - 1)
    
    def right(self) -> 'Position':
        return Position(self.y, self.x + 1)
    
    def top_left(self) -> 'Position':
        return Position(self.y - 1, self.x - 1)
    
    def top_right(self) -> 'Position':
        return Position(self.y - 1, self.x + 1)
    
    def bottom_left(self) -> 'Position':
        return Position(self.y + 1, self.x - 1)
    
    def bottom_right(self) -> 'Position':
        return Position(self.y + 1, self.x + 1)
    
    
    
    
class CellValue(IntEnum):
    EMPTY = 0
    ONEMINE = 1
    TWOMINE = 2
    THREEMINE = 3
    MINE = 4
    

@dataclass
class Cell:
    position: Position
    value : CellValue
    exposed: bool = False
    
    def is_empty_or_number(self) -> bool:
        return self.value in (CellValue.EMPTY, CellValue.ONEMINE, CellValue.TWOMINE, CellValue.THREEMINE)
    
    def is_number(self) -> bool:
        return self.value in (CellValue.ONEMINE, CellValue.TWOMINE, CellValue.THREEMINE)
    

class Board:
    size = 7
    mine_triggered: bool
    cells_till_victory: int
    layout: List[List[Cell]]
    
    def __init__(self) -> None:
        self.mine_triggered = False
        self.cells_till_victory = (self.size * self.size) - len(MINE_POSITIONS)
        self.layout = []
        for row_index in range(self.size):
            row: List[Cell] = []
            for column_index in range(self.size):
                position = Position(row_index, column_index)
                if any([p for p in MINE_POSITIONS if position.is_equal_to(p)]):
                    row.append(Cell(position=position, value=CellValue.MINE))
                elif any([p for p in ONE_MINE_POSITIONS if position.is_equal_to(p)]):
                    row.append(Cell(position=position, value=CellValue.ONEMINE))
                elif any([p for p in TWO_MINE_POSITIONS if position.is_equal_to(p)]):
                    row.append(Cell(position=position, value=CellValue.TWOMINE))
                else:
                    row.append(Cell(position=position, value=CellValue.EMPTY))
            self.layout.append(row)
            
    def get_cell_at_position(self, p: Position) -> Cell:
        return self.layout[p.y][p.x]
    
    def position_is_on_board(self, p: Position) -> bool:
        return p.y >= 0 and p.y < self.size and p.x >= 0 and p.x < self.size
    
    def uncover_position(self, p: Position, checked: List[Position] = []) -> None:
        if any([c for c in checked if p.is_equal_to(c)]):
            return
        position = self.get_cell_at_position(p)
        position.exposed = True
        self.cells_till_victory -= 1
        checked.append(p)
        if position.value == CellValue.MINE:
            self.mine_triggered = True
            return
        elif position.is_number():
            return
            
        if self.position_is_on_board(p.above()) and self.get_cell_at_position(p.above()).is_empty_or_number():
            self.uncover_position(p.above(), checked)
        if self.position_is_on_board(p.below()) and self.get_cell_at_position(p.below()).is_empty_or_number():
            self.uncover_position(p.below(), checked)
        if self.position_is_on_board(p.left()) and self.get_cell_at_position(p.left()).is_empty_or_number():
            self.uncover_position(p.left(), checked)
        if self.position_is_on_board(p.right()) and self.get_cell_at_position(p.right()).is_empty_or_number():
            self.uncover_position(p.right(), checked)
        if self.position_is_on_board(p.top_left()) and self.get_cell_at_position(p.top_left()).is_empty_or_number():
            self.uncover_position(p.top_left(), checked)
        if self.position_is_on_board(p.top_right()) and self.get_cell_at_position(p.top_right()).is_empty_or_number():
            self.uncover_position(p.top_right(), checked)
        if self.position_is_on_board(p.bottom_left()) and self.get_cell_at_position(p.bottom_left()).is_empty_or_number():
            self.uncover_position(p.bottom_left(), checked)
        if self.position_is_on_board(p.bottom_right()) and self.get_cell_at_position(p.bottom_right()).is_empty_or_number():
            self.uncover_position(p.bottom_right(), checked)
    
    def flag_position(self, p: Position) -> None:
        return
                

MINE_POSITIONS = [
    Position(1, 2),
    Position(3, 2),
    Position(6, 4)
]


ONE_MINE_POSITIONS = [
    Position(0, 1), Position(0, 2), Position(0, 3),
    Position(1, 1), Position(1, 3),
    Position(3, 1), Position(3, 3),
    Position(4, 1), Position(4, 2), Position(4, 3),
    Position(5, 3), Position(5, 4), Position(5, 5),
    Position(6, 3), Position(6, 5),
]


TWO_MINE_POSITIONS = [
    Position(2, 1), Position(2, 2), Position(3, 3),
]