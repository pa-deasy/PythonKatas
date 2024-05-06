def longest_palindrome(word: str) -> str:
    characters = list(word)
    reversed_characters = characters.copy()
    reversed_characters.reverse()
    grid = _generate_grid(word)
    
    longest_word = ''
    for row_index in range(0, len(grid)):
        for column_index in range(0, len(grid)):
            previous = _get_previous(grid, row_index, column_index)
            if characters[column_index] == reversed_characters[row_index]:
                palindrome_len = previous + 1
                grid[row_index][column_index] = palindrome_len
                if palindrome_len > len(longest_word):
                    longest_chars = characters[column_index - palindrome_len + 1: column_index + 1]
                    longest_word = ''.join(longest_chars)

    if len(longest_word) < 2:
        return ''
    
    return longest_word
    

def _generate_grid(word: str) -> list[list[int]]:
    grid_length = len(word)
    grid: list[list[int]] = []
    
    for row_index in range(0, grid_length):
        row = []
        for column_index in range(0, grid_length):
            row.append(0)
        grid.append(row)
        
    return grid


def _get_previous(grid: list[list[str]], row_index: int, column_index: int):
    if row_index - 1 >= 0 and column_index - 1 >= 0:
        return grid[row_index - 1][column_index - 1]
    else:
        return 0
