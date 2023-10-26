from dataclasses import dataclass
from typing import List


# 10.1 - Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted Order.
def sorted_merge(a: List[int], b: List[int]) -> List[int]:
    a_index = len(a) - len(b) - 1
    b_index = len(b) - 1
    end_index = len(a) - 1
    
    while b_index >= 0:
        if a_index >= 0 and a[a_index] > b[b_index]:
            a[end_index] = a[a_index]
            a_index -= 1
        else:
            a[end_index] = b[b_index]
            b_index -= 1
        end_index -= 1
        
    return a


# 10.2 - Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.
@dataclass
class Anagram:
    raw: str
    sorted: str
    

def group_anagrams(input: List[str]) -> List[str]:
    anagrams = [Anagram(raw=i, sorted=''.join(sorted(i))) for i in input]
    
    anagrams.sort(key=lambda a: a.sorted)
    
    return [a.raw for a in anagrams]


# 10.3 - Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array.
# You may assume that the array was originally sorted in increasing order.
# Find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], output of 8
def search_rotated_array(numbers: List[int], target: int) -> int:
    return search_rotated(numbers, target, 0, len(numbers) - 1)

def search_rotated(numbers: List[int], target: int, left: int, right: int) -> int:
    middle = round((left + right) / 2)
    
    if target == numbers[middle]:
        return middle
    
    if numbers[left] < numbers[middle]:
        if numbers[left] <= target and target < numbers[middle]:
            return search_rotated(numbers, target, left, middle - 1)
        else:
            return search_rotated(numbers, target, middle + 1, right)
    elif numbers[middle] < numbers[right]:
        if numbers[middle] < target and target <= numbers[right]:
            return search_rotated(numbers, target, middle + 1, right)
        else:
            return search_rotated(numbers, target, left, middle - 1)
    else:
        location = None
        if numbers[left] == numbers[middle]:
            location = search_rotated(numbers, target, middle + 1, right)
        if location is None and numbers[middle] == numbers[right]:
            location = search_rotated(numbers, target, left, middle - 1)
        else:
            return location
        
        
# 10.4 - Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size method. It does however have a elementAt(i) method that returns the element
# at index i in O(1) time. If i is beyond the bounds of the data structure, it returns -1(for this reason the data structure only supports positive integers). 
# Given a Listy which contains, sorted, positive integers, find the index at which and element x occurs. If x occurs multiple times, you may return any index.
class Listy:
    values: List[int]
    
    def __init__(self, values: List[int]) -> None:
        self.values = sorted(values)
    
    def element_at(self, index: int) -> int:
        if 0 > index or index > len(self.values) - 1:
            return -1
        return self.values[index]
    
    def index_of(self, target: int) -> int:
        index = 1
        while self.element_at(index) != -1 and self.element_at(index) < target:
            index *= 2
        
        return self.binary_search(target, round(index / 2), index)
    
    def binary_search(self, target: int, low: int, high: int) -> int:
        if low > high:
            return None

        mid = round((low + high) / 2)
        if self.element_at(mid) == target:
            return mid
        elif self.element_at(mid) < target:
            return self.binary_search(target, mid + 1, high)
        else:
            return self.binary_search(target, low, mid - 1)
    

# 10.5 - Sparse Search: Given a sorted array of strings that is interspersed with empty string, write a method to find the location of a given string.
# ball -> ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''] -> 4
def sparse_search(words: List[str], target: str) -> int:
    low = 0
    high = len(words) - 1
    
    while low <= high:
        mid = round((low + high) / 2)
        
        while not words[mid] and mid < high:
            mid += 1
        
        if words[mid] == target:
            return mid
        elif not words[mid] or words[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
            


# 10.8 - Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000. The array may have duplicate entries and you do not know what N is.
# With only 4 kilobytes of memory available, how would you print all duplicate elements in the array?
class BitSet():
    bitset: List[int]
    
    def __init__(self, size: int) -> None:
        self.bitset = [None for i in range((size >> 5) + 1)]
    
    def get(self, index: int) -> bool:
        word_number = index >> 5
        bit_number = index % 32
        return (self.bitset[word_number] and (1 << bit_number)) != 0 
    
    def set(self, index: int) -> None:
        word_number = index >> 5
        bit_number = index % 32
        self.bitset[word_number] |= 1 << bit_number
    
    
def check_duplicates(numbers: List[int]) -> List[int]:
    bitset = BitSet(32000)
    duplicates: List[int] = []
    
    for number in numbers:
        number0 = number - 1
        if bitset.get(number0):
            print(f'{number} is a duplicate')
            duplicates.append(number)
            
        else:
            bitset.set(number0)
            
    return duplicates


# 10.9 - Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.
@dataclass
class MatrixPosition:
    row: int
    column: int
    

def search_matrix(matrix: List[List[int]], target: int) -> MatrixPosition:
    row = _find_target_row(matrix, target)
    return _find_target_on_row(matrix, target, row) if row else None
    

def _find_target_row(matrix: List[List[int]], target: int) -> int:
    low = 0
    high = len(matrix) - 2
    while low <= high:
        mid = round((low + high) / 2)
        
        if matrix[mid][0] <= target and target < matrix[mid + 1][0]:
            return mid
        elif matrix[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return None


def _find_target_on_row(matrix: List[List[int]], target: int, row: int) -> MatrixPosition:
    low = 0
    high = len(matrix[row]) - 1
    while low <= high:
        mid = round((low + high) / 2)
        
        if matrix[row][mid] == target:
            return MatrixPosition(row=row, column=mid)
        elif matrix[row][mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return None


        # [1, 2, 3, 4, 5],
        # [6, 7, 8, 9, 10],
        # [11, 12, 13, 14, 15],
        # [16, 17, 18, 19, 20]
        
        # 14