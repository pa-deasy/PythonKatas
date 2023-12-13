from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Set

from stacks_and_queues.stacks_and_queues_examples import Stack


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
    
    
# 8.5 - Recursive Multipy: Write a recursive function to multiply two positive integers without using the * operator. You can use addition, subtraction and bit shifting,
# but you should minimize the number of those operations.
def recursive_multiply(a: int, b: int, sum: int = 0) -> int:
    if b == 0:
        return sum
    
    return recursive_multiply(a, b - 1, sum + a)


def recurse_multiply_efficient(a: int, b: int) -> int:
    smaller, bigger = (a, b) if a < b else (b, a)
    return _recurse_multiply_efficient(smaller, bigger)


def _recurse_multiply_efficient(smaller: int, bigger: int) -> int:
    if smaller == 0:
        return 0
    
    if smaller == 1:
        return bigger
    
    s = round(smaller / 2)
    half_prod = _recurse_multiply_efficient(s, bigger)
    
    if smaller % 2 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger 
    

# 8.6 - Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide ont any tower. The puzzle starts 
# with disks sorted in ascending order of size from top to bottom (i.e each disk sits on top of an even larger one). You have the following constraints:
# 1. Only one disk can be moved at a time.
# 2. A disk is slid off the top of one tower and onto another tower.
# 3. A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using Stacks.
class Tower:
    disks: Stack
    
    def __init__(self) -> None:
        self.disks = Stack()
        
    def add(self, d: int) -> None:
        if not self.disks.is_empty() and self.disks.peek() <= d:
            raise Exception('Disk cannot be placed on a smaller disk')
        else:
            self.disks.push(d)
            
    def move_top_to(self, t: 'Tower') -> None:
        top = self.disks.pop()
        t.add(top)
        
    def move_disks(self, quantity: int, destination: 'Tower', buffer: 'Tower') -> None:
        if quantity <= 0:
            return
        
        self.move_disks(quantity - 1, buffer, destination)
        self.move_top_to(destination)
        buffer.move_disks(quantity - 1, destination, self)
        

# 8.7 - Permutations Without Dups: Write a method to compute all permutations of a string of unique characters.
def all_permutations(word: str) -> List[str]:
    return _all_permutations(word, '', [])


def _all_permutations(remaining: str, prefix: str, permutations: List[str]) -> List[str]:
    if not remaining:
        permutations.append(prefix)
        return permutations
    
    for index in range(len(remaining)):
        new_remaining = remaining[:index] + remaining[index + 1:]
        new_prefix = prefix + remaining[index]
        _all_permutations(new_remaining, new_prefix, permutations)
        
    return permutations


def _other_all_permutations(remaining: str, prefix: str, permutations: List[str]) -> List[str]:
    if not remaining:
        permutations.append(prefix)
        return permutations
    
    popped = remaining[:1]
    new_remaining = remaining[1:]
    
    if not prefix:
        return _all_permutations(new_remaining, popped, permutations)
    
    for index in range(len(prefix) + 1):
        new_prefix = prefix[:index] + popped + prefix[index:]
        _all_permutations(new_remaining, new_prefix, permutations)
        
    return permutations


# 8.8 - Permutations With Dups: Write a method to compute all permutations of a string whose characters are not necessarily unique.
# The list should not have duplicate.
def all_permutations_with_dups(word: str) -> List[str]:
    char_counts = _get_char_counts(word)
    return _all_permutations_with_dups(char_counts, '', len(word), [])


def _all_permutations_with_dups(char_count: Dict[str, int], prefix: str, remaining: int, permutations: List[str]) -> List[str]:
    if remaining == 0:
        permutations.append(prefix)
        return permutations
    
    for c in char_count.keys():
        count = char_count.get(c)
        if count > 0:
            char_count[c] = count - 1
            _all_permutations_with_dups(char_count, prefix + c, remaining - 1, permutations)
            char_count[c] = count
        
    return permutations

def _get_char_counts(word: str) -> Dict[str, int]:
    char_counts: Dict[str: int] = {}
    for char in list(word):
        count = char_counts.get(char)
        char_counts[char] = 1 if not count else count + 1
        
    return char_counts


# 8.9 - Parens: Implement an algorithm to print all valid (e.g. properly opened and closed) combinations of n pairs of parentheses.
# Input 3 -> ((())), (()()), (())(), ()(()), ()()()
def parens_permutations(parens_count: int, parens: List[str] = None) -> List[str]:
    parens: List[str] = []
    
    _add_paren(parens, parens_count, parens_count, '')
    
    return parens
    
    
def _add_paren(parens: List[str], left_rem: int, right_rem: int, current: str) -> None:
    if left_rem < 0 or right_rem < left_rem:
        return 
    elif left_rem == 0 and right_rem == 0:
        parens.append(current)
        return
    
    
    add_left = current + '('
    _add_paren(parens, left_rem - 1, right_rem, add_left)
    
    add_right = current + ')'
    _add_paren(parens, left_rem, right_rem - 1, add_right)
