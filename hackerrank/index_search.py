import math


def index_search(numbers: list[int], target: int) -> int:
    return _binary_search(numbers, target)

def _binary_search(numbers: list[int], target: int) -> int:
    low = 0
    high = len(numbers) - 1
    
    while low <= high:
        mid = round((low + high) / 2)
        guess = numbers[mid]
        
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1