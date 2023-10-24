from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    for right_index in range(len(numbers), -1, -1):
        for left_index in range(right_index - 1):
            if numbers[left_index] > numbers[left_index + 1]:
                numbers[left_index], numbers[left_index + 1] = numbers[left_index + 1], numbers[left_index]
    return numbers
   


    # numbers = [-2, 45, 0, 11, -9]
    # expected = [-9, -2, 0, 11, 45]