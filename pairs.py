from typing import Dict

def pairs_with_diff_summing_to(target: int, numbers: list[int]) -> int:
    numbers_count = _count_numbers(numbers)
    count_of_pairs = 0
    
    for key in numbers_count.keys():
        diff = abs(key - target)
        if diff != key and numbers_count.get(diff):
            count_of_pairs += 1
            
    return count_of_pairs
        

def _count_numbers(numbers: list[int]) -> Dict[int, int]:
    numbers_count: Dict[int, int] = {}
    for number in numbers:
        if numbers_count.get(number):
            numbers_count[number] += 1
        else:
            numbers_count[number] = 1
    return numbers_count
