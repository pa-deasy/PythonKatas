def insertion_sort(numbers):
    for right_index in range(1, len(numbers)):
        left_index = right_index - 1
        right_number = numbers[right_index]
        while left_index >= 0 and numbers[left_index] > right_number:
            numbers[left_index + 1] = numbers[left_index]
            left_index -= 1
        numbers[left_index + 1] = right_number
    
    return numbers