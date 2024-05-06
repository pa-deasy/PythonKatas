from sys import maxsize


def closest_pair_to_sum(numbers: list[int], target_sum: int) -> tuple[int, int]:
    
    sorted_numbers = _quicksort(numbers)
    
    left_index, right_index = 0, len(sorted_numbers) - 1
    closest_sum = maxsize
    closest_first, closest_second = sorted_numbers[left_index], sorted_numbers[right_index]
    
    while left_index < right_index:
        sum = sorted_numbers[left_index] + sorted_numbers[right_index]
        
        if abs(target_sum - sum) < abs(target_sum - closest_sum):
            closest_first, closest_second = sorted_numbers[left_index], sorted_numbers[right_index]
            closest_sum = sum
            
        if sum < target_sum:
            left_index += 1
        else:
            right_index -= 1
        
    return closest_first, closest_second


def _quicksort(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers
    
    pivot = numbers.pop(0)
    greater_than = [n for n in numbers if n > pivot]
    less_than_equal = [n for n in numbers if n <= pivot]
    
    return _quicksort(less_than_equal) + [pivot] + _quicksort(greater_than)
