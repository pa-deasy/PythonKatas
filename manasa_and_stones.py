def predict_values_of_last_stone(stones_count: int, stone_diff_a: int, stone_diff_b: int) -> list[int]:
    possible_values = set([stone_diff_a, stone_diff_b])

    for index in range(stones_count - 2):
        next_possible_values: set[int] = set()
        for value in possible_values:
            next_possible_values.add(value + stone_diff_a)
            next_possible_values.add(value + stone_diff_b)
            possible_values = next_possible_values
    
    predicted_values = list(possible_values)
    predicted_values.sort()
    return predicted_values
