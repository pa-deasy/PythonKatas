def quicksort(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers
    
    pivot = numbers.pop(0)
    
    less_than_equal = [num for num in numbers if num <= pivot]
    greater_than = [num for num in numbers if num > pivot]
    
    return quicksort(less_than_equal) + [pivot] + quicksort(greater_than)


def mergesort(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers
    
    half_index = round(len(numbers) / 2)    
    left = numbers[:half_index]
    right = numbers[half_index:]
    
    return _merge(mergesort(left), mergesort(right))

    
def _merge(left: list[int], right: list[int]) -> list[int]:
    merged_numbers: list[int] = []
    
    while(left):
        if not right or left[0] < right[0]:
            merged_numbers.append(left.pop(0))            
        else:
            merged_numbers.append(right.pop(0))
            
    if right:
        merged_numbers = merged_numbers + right
        
    return merged_numbers
