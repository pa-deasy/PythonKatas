def get_missing_number(numbers: list[int]) -> int:
    n = len(numbers) + 1
    expected_sum = (n * (n + 1) / 2)
    actual_sum = sum(numbers)
    
    return expected_sum - actual_sum
    