from typing import Any


def rotate_array(array: list[Any], rotations: int, indexes: list[int]) -> list[Any]:
    array_length = len(array)
    return [array[(index - rotations + array_length) % array_length] for index in indexes]


def non_optimal_rotate_array(array: list[Any], rotations: int, indexes: list[int]) -> list[Any]:
    rotations = rotations % len(array)
    for rotation in range(rotations):
        popped = array.pop()
        array = [popped] + array
    
    return_array = []
    for index in indexes:
        return_array.append(array[index])
        
    return return_array




# pytest.param([3, 4, 5], 2, [1, 2], [5, 3])