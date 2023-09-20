# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. 
def urlify(chars: list[str], true_length: int) -> str:
    space_count = _count_in(chars, 0, true_length, ' ')
    new_index = true_length - 1 + space_count * 2
    
    for increase_index in range(len(chars), new_index + 1):
        chars.append('')
    
    for old_index in range(true_length -1, -1, -1):
        if chars[old_index] == ' ':
            chars[new_index] = '0'
            chars[new_index - 1] = '2'
            chars[new_index - 2] = '%'
            new_index -= 3
        else:
            chars[new_index] = chars[old_index]
            new_index -= 1
    
    return chars


def _count_in(chars: list[str], start: int, end: int, target: str) -> int:
    count = 0
    for char in chars[start:end]:
        if char == target:
            count += 1
    return count
