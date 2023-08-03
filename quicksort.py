def quicksort_numbers(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers
    
    pivot = numbers[0]
    
    less_than = [n for n in numbers[1:] if n < pivot]
    greater_than_equal = [n for n in numbers[1:] if n >= pivot]
    
    return quicksort_numbers(less_than) + [pivot] + quicksort_numbers(greater_than_equal)
