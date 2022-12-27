from typing import List, Optional


def simple_search_index(search_number: int, search_list: list[int]) -> Optional[int]:
    position = 0
    search_list_lenght = len(search_list)
    
    while position < search_list_lenght:
        if search_list[position] == search_number:
            return position
        
        else:
            position += 1
            
    return None
