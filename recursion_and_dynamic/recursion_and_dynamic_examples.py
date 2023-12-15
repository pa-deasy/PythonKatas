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
def parens_permutations(parens_count: int) -> List[str]:
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
    
    
# 8.10 - Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.
@dataclass
class Point:
    y: int
    x: int

    def is_on_canvas(self, size: int) -> bool:
        return 0 <= self.y < size and 0 <= self.x < size

    def above(self) -> 'Point':
        return Point(self.y - 1, self.x)

    def below(self) -> 'Point':
        return Point(self.y + 1, self.x)

    def left(self) -> 'Point':
        return Point(self.y, self.x - 1)

    def right(self) -> 'Point':
        return Point(self.y, self.x + 1)


class Canvas:
    size: int
    layout: List[List[str]]

    def __init__(self, size: int) -> None:
        self.size = size

        rows = []
        for index in range(size):
            row = [None] * size
            rows.append(row)

        self.layout = rows

    def fill_with_color(self, color: str, point: Point) -> None:
        old_color = self.layout[point.y][point.x]
        if old_color == color:
            return

        self._fill_with_color(color, old_color, point)

    def _fill_with_color(self, color: str, old_color: str, point: Point) -> None:
        if not point.is_on_canvas(self.size) or self.layout[point.y][point.x] != old_color:
            return

        self.layout[point.y][point.x] = color

        self._fill_with_color(color, old_color, point.above())
        self._fill_with_color(color, old_color, point.below())
        self._fill_with_color(color, old_color, point.left())
        self._fill_with_color(color, old_color, point.right())


# 8.11 - Coins: Given an infinite number of quarters(25 cents), dimes(10 cents), nickels(5 cents), and pennies(1 cent),
# write code to calculate the number of ways of representing n cents.
@dataclass
class Coins:
    pennies: int = 0
    nickels: int = 0
    dimes: int = 0
    quarters: int = 0


def permutations_of_cents(total_cents: int) -> List[Coins]:
    permutations: List[Coins] = []
    _permutations_of_cents(total_cents, Coins(), permutations)

    return permutations


def _permutations_of_cents(total_cents: int, coins: Coins, permutations: List[Coins]) -> None:
    if total_cents < 0:
        return

    if total_cents == 0:
        if coins not in permutations:
            permutations.append(coins)
        return

    with_penny = Coins(pennies=coins.pennies + 1, nickels=coins.nickels, dimes=coins.dimes, quarters=coins.quarters)
    _permutations_of_cents(total_cents - 1, with_penny, permutations)

    with_nickel = Coins(pennies=coins.pennies, nickels=coins.nickels + 1, dimes=coins.dimes, quarters=coins.quarters)
    _permutations_of_cents(total_cents - 5, with_nickel, permutations)

    with_dimes = Coins(pennies=coins.pennies, nickels=coins.nickels, dimes=coins.dimes + 1, quarters=coins.quarters)
    _permutations_of_cents(total_cents - 10, with_dimes, permutations)

    with_quarters = Coins(pennies=coins.pennies, nickels=coins.nickels, dimes=coins.dimes, quarters=coins.quarters + 1)
    _permutations_of_cents(total_cents - 25, with_quarters, permutations)


# 8.12 - Eight Queens: Write an algorithm to print all the ways of arranging eight queens on an 8 x 8 chess board so that none of them share the same row, column, or diagonal.
# In this case diagonal means all diagonals, not just the two that bisect the board.
GRID_SIZE = 8

def permutations_of_queens() -> List[List[int]]:
    columns = [None] * GRID_SIZE
    permutations: List[List[int]] = []
    _permutations_of_queens(0, columns, permutations)
    
    return permutations
    
    
def _permutations_of_queens(row: int, columns: List[int], permuations: List[List[int]]) -> None:
    if row == GRID_SIZE:
        permuations.append(list(columns))
        return
    
    for column in range(GRID_SIZE):
        if _check_is_valid(row, column, columns):
            columns[row] = column
            _permutations_of_queens(row + 1, columns, permuations)
        
        
def _check_is_valid(row: int, column: int, columns: List[int]) -> bool:
    for other_row in range(0, row):
        other_column = columns[other_row]
        
        if column == other_column:
            return False
        
        column_diff = abs(other_column - column)
        row_diff = abs(row - other_row)
        
        if column_diff == row_diff:
            return False
        
    return True
    

# 8.13 - Stack of Boxes: You have a stack of n boxes, with widths w, heights h, and depts d. The boxes cannot be rotated and can only be stacked on
# top of one another if each box in the stack is strictly larger than the box above it in width, height and depth. Implement a method to compute the height
# of the tallest possible stack. The height of the stack is the sum of the heights of each box.
@dataclass
class Box:
    width: int
    height: int
    dept: int

def calculate_highest_stack(boxes: List[Box]) -> int:
    boxes.sort(key=lambda b: b.height, reverse=True)
    
    max_height = 0
    stack_map: List[int] = [None] * len(boxes)
    for index in range(len(boxes)):
        height = _calculate_highest_stack(boxes, index, stack_map)
        max_height = max(max_height, height)
        
    return max_height
        
    
def _calculate_highest_stack(boxes: List[Box], bottom_index: int, stack_map: List[int]) -> int:
    if stack_map[bottom_index] is not None:
        return stack_map[bottom_index]
    
    bottom = boxes[bottom_index]
    max_height = 0
    
    for index in range(bottom_index + 1, len(boxes)):
        if _can_be_above(boxes[index], bottom):
            height = _calculate_highest_stack(boxes, index, stack_map)
            max_height = max(max_height, height)
    
    max_height += bottom.height
    stack_map[bottom_index] = max_height
    return max_height
    

def _can_be_above(top: Box, bottom: Box) -> bool:
    return top.width < bottom.width and top.height < bottom.height and top.dept < bottom.dept


# 8.14 - Boolean Evaluation: Given a boolean expression consisting of the symbols:
# 0(false), 1(true), &(AND), |(OR), ^(XOR)
# and a desired boolean result value, implement a function to count the number of ways of parenthesizing the expression such that it evaluates to result.
# The expression should be fully parenthesized (e.g. (0)^(1) but not extraneously (e.g. (((0)^(1))).
# count_eval('1^0|0|1', False) -> 2
# count_eval('0&0&0&1^1|0', True) -> 10
def count_eval(symbols: str, result: bool) -> int:
    if len(symbols) == 0:
        return 0
    if len(symbols) == 1:
        return 1 if _symbol_to_boolean(symbols) == result else 0

    ways = 0
    for index in range(1, len(symbols), 2):
        char = symbols[index]
        left = symbols[:index]
        right = symbols[index + 1:]

        left_true = count_eval(left, True)
        left_false = count_eval(left, False)
        right_true = count_eval(right, True)
        right_false = count_eval(right, False)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if char == '^':
            total_true = left_true * right_false + left_false * right_true
        elif char == '&':
            total_true = left_true * right_true
        elif char == '|':
            total_true == left_true * right_true + left_false * right_true + left_true * right_false

        sub_ways = total_true if result else total - total_true
        ways += sub_ways

    return ways


def _symbol_to_boolean(symbol: str) -> bool:
    return symbol == '1'
