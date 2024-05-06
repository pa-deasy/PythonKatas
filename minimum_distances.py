from typing import Optional


def minimum_distance(numbers: list[int]) -> int:
    number_indices = _get_number_indices(numbers)
    minimum_distance: Optional[int] = None
    
    for indices in number_indices.values():
        if len(indices) == 2:
            distance = indices[1] - indices[0]
            minimum_distance = distance if not minimum_distance or distance < minimum_distance else minimum_distance
    
    return minimum_distance if minimum_distance else -1
    


def _get_number_indices(numbers: list) -> dict[int, list[int]]:
    number_indices: dict[int, list[int]] = {}
    for index in range(len(numbers)):
        number = numbers[index]
        indices = number_indices.get(number)
        if indices:
            indices.append(index)
            number_indices[number] = indices
        else:
            number_indices[number] = [index]
            
    return number_indices