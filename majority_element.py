from typing import Optional


def get_majority_element(numbers: list[int]) -> Optional[int]:
    numbers_counts: dict[int, int] = {}
    minority_count = int(len(numbers) / 2)
    
    for index in range(0, len(numbers)):
        number = numbers[index]
        number_count = numbers_counts.get(number) + 1 if numbers_counts.get(number) else 1
        
        numbers_counts[number] = number_count
        
        if number_count > minority_count:
            return number
    
    return None
