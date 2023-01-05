def remove_duplicate_chars_and_order(input: str) -> str:
    unique_chars = list(set(input))
    
    unique_sorted_chars = _merge_sort(unique_chars)
    
    return ''.join(unique_sorted_chars)


def _merge_sort(chars: list[str]) -> list[str]:
    if len(chars) < 2:
        return chars
    
    halfway = round(len(chars) / 2)
    left = chars[:halfway]
    right = chars[halfway:]
    
    return _merge(_merge_sort(left), _merge_sort(right))
    
    
def _merge(left: list[str], right: list[str]) -> list[str]:
    merged: list[str] = []
    
    while left:
        if not right or left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
            
    if right:
        merged += right
        
    return merged
    