from sys import maxsize


def largest_contiguous_sum_of(numbers: list[int]) -> int:
    current_sum = 0
    largest_sum = -maxsize
    
    for number in numbers:
        if number > current_sum and current_sum < 0:
            current_sum = number
        else:
            current_sum += number
        
        if current_sum > largest_sum:
            largest_sum = current_sum
            

    return largest_sum
    