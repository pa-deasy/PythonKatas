def longest_common_substring(first_word: str, second_word: str) -> int:
    first_word_array = list(first_word)
    second_word_array = list(second_word)
    grid = _generate_grid(first_word, second_word)
    max_substring_count = 0
    
    for first_word_index in range(len(first_word)):
         for second_word_index in range(len(second_word)):
            substring_count = 0
             
            if first_word_array[first_word_index] == second_word_array[second_word_index]:
                substring_count = 1
                if first_word_index - 1 >= 0 and second_word_index - 1 >= 0:
                    substring_count += grid[first_word_index - 1][second_word_index - 1]
            
            grid[first_word_index][second_word_index] = substring_count
            
            max_substring_count = max(max_substring_count, substring_count)
    
    return max_substring_count


def longest_common_sequence(first_word: str, second_word: str) -> int:
    first_word_array = list(first_word)
    second_word_array = list(second_word)
    grid = _generate_grid(first_word, second_word)
    
    for first_word_index in range(len(first_word)):
        for second_word_index in range(len(second_word)):
            sequence_count = 0
            
            if first_word_array[first_word_index] == second_word_array[second_word_index]:
                sequence_count += 1
                if first_word_index - 1 >= 0 and second_word_index - 1 >= 0:
                    sequence_count += grid[first_word_index - 1][second_word_index - 1]
            else:
                left = grid[first_word_index][second_word_index - 1] if second_word_index - 1 >= 0 else 0
                above = grid[first_word_index - 1][second_word_index] if first_word_index -1 >= 0 else 0
                sequence_count = max(left, above)
                
            grid[first_word_index][second_word_index] = sequence_count
    
    return grid[len(first_word) - 1][len(second_word) - 1]


def _generate_grid(first_word: str, second_word: str) -> list[list[int]]:
    grid = []
    for first_word_index in range(len(first_word)):
        row = []
        for second_word_index in range(len(second_word)):
            row.append(0)
        grid.append(row)
    return grid
    