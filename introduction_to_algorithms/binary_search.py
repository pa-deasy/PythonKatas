from typing import Optional


def binary_search_index(search_number: int, search_list: list[int]) -> Optional[int]:    
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = round((low + high) / 2)
        guess = search_list[mid]
        
        if guess == search_number:
            return mid
        
        if guess < search_number:
            low = mid + 1
        
        else:
            high = mid -1
            
    return None
            