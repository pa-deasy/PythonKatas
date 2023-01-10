def pair_summing_to(target: int, numbers: list[int]) -> tuple[int, int]:
    while numbers:
        number = numbers.pop()
        diff = target - number
        
        if diff in numbers:
            return number, diff
            
    return 0


def triple_summing_to(target: int, numbers: list[int]) -> tuple[int, int]:
    for first_index in range(0, len(numbers) - 1):
        first_number = numbers[first_index]
        for second_index in range(first_index + 1, len(numbers)):
            second_number = numbers[second_index]
            diff = target - first_number - second_number

            remaining = numbers[second_index + 1:]
            if diff in remaining:
                return first_number, second_number, diff
            
    return 0