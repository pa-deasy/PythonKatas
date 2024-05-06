from dataclasses import dataclass
from enum import IntEnum
from typing import Dict, List


# 16.1 - Number Swapper: Write a function to swap two numbers in place(that is, without temporary variables)
def swap_numbers(numbers: List[int], first_index: int, second_index: int) -> None:
    if first_index == second_index or first_index >= len(numbers) or second_index >= len(numbers):
        return

    numbers[second_index] += numbers[first_index]
    numbers[first_index] = numbers[second_index] - numbers[first_index]
    numbers[second_index] -= numbers[first_index]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 5, 5]
# [4, 2, 3, 5, 5]
# [4, 2, 3, 1, 5]
    

# 16.2 - Word Frequencies: Design a method to find the frequency of occurrences of any given word in a book. 
# What if we were running this algorithm multiple times?
@dataclass
class Page:
    number: int
    content: str
    

class Book:
    pages: List[Page]
    word_occurrences: Dict[str, int]
    
    def __init__(self, pages: List[Page]) -> None:
        self.pages = pages
        self._populate_word_occurences()
        
    def _populate_word_occurences(self) -> None:
        self.word_occurrences = {}
        for page in self.pages:
            words = page.content.split(' ')
            for word in words:
                word = word.lower()
                self.word_occurrences[word] = self.word_occurrences.get(word, 0) + 1
        
    def count_occurrences_of(self, search_word: str) -> int:
        return self.word_occurrences.get(search_word.lower(), 0)


# 16.3 - Intersection: Given two straight line segments(represented as a start point and an end point), compute the point of intersection if any.
@dataclass
class Point:
    y: int
    x: int
    

@dataclass
class Line:
    start: Point
    end: Point
    

def find_point_of_intersection(a: Point, b: Point) -> Point:
    return None


# 16.4 - TicTacWin: Design an algorithm to figure out if someone has won a game of tic-tac-toe.
class Player(IntEnum):
    X = 0
    O = 1
    

@dataclass
class Move:
    player: Player
    row: int
    column: int
    

class TicTacToe:
    layout: List[List[Player]]
    
    def __init__(self, layout: List[List[Player]]) -> None:
        self.layout = layout

    def is_won(self, move: Move) -> bool:
        return self._row_is_won(move) or self._column_is_won(move) or self._diagonal_is_won(move)
    
    def _row_is_won(self, move: Move) -> bool:
        return self.layout[move.row][0] == move.player and self.layout[move.row][1] == move.player and self.layout[move.row][2] == move.player

    def _column_is_won(self, move: Move) -> bool:
        return self.layout[0][move.column] == move.player and self.layout[1][move.column] == move.player and self.layout[2][move.column] == move.player

    def _diagonal_is_won(self, move: Move) -> bool:
        if (move.row in (0, 2) and move.column in (0, 2)) or (move.row == 1 and move.column == 1):
            return (self.layout[0][0] == move.player and self.layout[1][1] == move.player and self.layout[2][2] == move.player) or (self.layout[0][2] == move.player and self.layout[1][1] == move.player and self.layout[2][0])
        return False
    


# 16.5 - Factorial Zeros: Write an algorithms which computes the number of trailing zeros in a factorial.