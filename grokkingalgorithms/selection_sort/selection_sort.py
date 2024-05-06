


from typing import Optional


def selection_sort(numbers: list[int]) -> list[int]:
    reordered_numbers: list[int] = []
    
    while numbers:
        largest_number_index = _largest_number_index(numbers)
        reordered_numbers.append(numbers.pop(largest_number_index))
        
    return reordered_numbers


def _largest_number_index(numbers: list[int]) -> int:
    
    index = 0
    largest_number_index = index
    
    while index < len(numbers):
        if numbers[index] > numbers[largest_number_index]:
            largest_number_index = index
            
        index += 1
        
    return largest_number_index
            
    