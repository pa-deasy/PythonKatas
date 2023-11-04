from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Set


def fibonacci(i: int, memo: Dict[int, int] = {}) -> int:
    if i == 0 or i == 1:
        return i
    
    if not memo.get(i):
        memo[i] = fibonacci(i - 1, memo) + fibonacci(i - 2, memo)
    
    return memo.get(i)


# 8.1 - Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up the stairs.
def count_ways(step: int, memo: Dict[int, int] = {}) -> int:
    if step < 0:
        return 0
    elif step == 0:
        return 1
    
    if not memo.get(step):
        memo[step] = count_ways(step - 1, memo) + count_ways(step - 2, memo) + count_ways(step - 3, memo)
    
    return memo.get(step) 


# 8.2 - Robot in a Grid: Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down,
# but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
class CellValue(Enum):
    PASS = 'pass'
    BLOCK = 'block'
    

@dataclass
class Position:
    row: int
    column: int
    
    def move_down(self) -> 'Position':
        return Position(row=self.row + 1, column=self.column)
    
    def move_right(self) -> 'Position':
        return Position(row=self.row, column=self.column + 1)
    

class RobotGrid:
    layout: List[List[CellValue]]
    
    def __init__(self) -> None:
        self.layout = [
            [CellValue.PASS, CellValue.BLOCK, CellValue.PASS, CellValue.PASS],
            [CellValue.PASS, CellValue.BLOCK, CellValue.PASS, CellValue.PASS],
            [CellValue.PASS, CellValue.BLOCK, CellValue.PASS, CellValue.PASS],
            [CellValue.PASS, CellValue.PASS, CellValue.PASS, CellValue.PASS],
        ]
    
    def target_reached(self, position: Position) -> bool:
        return True if position.row == len(self.layout) - 1 and position.column == len(self.layout[0]) - 1 else False
    
    def can_move_down(self, position: Position) -> bool:
        return True if position.row + 1 < len(self.layout) and self.layout[position.row + 1][position.column] == CellValue.PASS else False
    
    def can_move_right(self, position: Position) -> bool:
        return True if position.column + 1 < len(self.layout[0]) and self.layout[position.row][position.column + 1] == CellValue.PASS else False
    
    def get_path(self, position: Position = Position(row=0, column=0), path: List[Position] = []) -> List[Position]:
        this_path = path.copy()
        this_path.append(position)
        
        down = None
        right = None
        if self.target_reached(position):
            return this_path
        if self.can_move_down(position):
            down = self.get_path(position.move_down(), this_path)
        if self.can_move_right(position):
            right = self.get_path(position.move_right(), this_path)
            
        return down if down else right
            

# 8.3 - Magic Index: A magic index in an Array A[0...n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# What if the values are not distinct.
def find_magic_index(numbers: List[int], low: int, high: int) -> Optional[int]:
    mid = round((low + high) / 2)
    if high < low:
        return None
    elif numbers[mid] == mid:
        return mid
    elif numbers[mid] > mid:
        return find_magic_index(numbers, low, mid - 1)
    else:
        return find_magic_index(numbers, mid + 1, high)


def find_magic_index_with_duplicates(numbers: List[int], low: int, high: int) -> Optional[int]:
    mid = round((low + high) / 2)
    mid_value = numbers[mid]
    
    if mid_value == mid:
        return mid
    
    # search left
    left_index = min(mid - 1, mid_value)
    left = find_magic_index_with_duplicates(numbers, low, left_index)
    if left:
        return left
    
    # search right
    right_index = max(mid + 1, mid_value)
    right = find_magic_index_with_duplicates(numbers, right_index, high)
    return right


# 8.4 - Power Set: Write a method to return all subsets of a set
def all_subsets_of(numbers: List[int], subsets: List[List[int]] = [[]]) -> List[List[int]]:
    if not numbers:
        return subsets
    
    n = numbers.pop(0)
    new_subsets = []
    for s in subsets:
        new = s.copy()
        new.append(n)
        new_subsets.append(new)
    
    return all_subsets_of(numbers, subsets + new_subsets)
    
    