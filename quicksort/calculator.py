


def add(total: int, numbers: list[int]) -> int:
    if not numbers:
        return total
    
    total += numbers.pop()
    
    return add(total, numbers)