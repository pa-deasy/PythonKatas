from typing import Dict

# 1.1 - Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures
def is_unique(word: str) -> bool:
    return len(set(word)) == len(word)


def is_unique_no_datastructures(word: str) -> bool:
    chars = list(word)
    chars.sort()
    for left_index in range(len(chars) - 1):
        right_index = left_index + 1
        if chars[left_index] == chars[right_index]:
            return False
    return True


def is_unique_no_datastructures_other(word: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ord_offset = 97

    for index in range(len(word)):
        char = word[index]
        alphabet_pos = ord(char) - ord_offset
        if alphabet[alphabet_pos] != char:
            return False
        else:
            alphabet = alphabet[:alphabet_pos] + '!' + alphabet[alphabet_pos + 1:]
    return True


# 1.2 - Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
def is_permutation(word: str, potential_permutation: str) -> bool:
    # permutations = _get_permutations(word)
    # return True if potential_permutation in permutations else False

    word_char_count = _to_char_count(word)
    potential_char_count = _to_char_count(potential_permutation)

    for key, value in word_char_count.items():
        potential_char_count_value = potential_char_count.get(key)

        if not potential_char_count_value or potential_char_count_value != value:
            return False
    return True


def _to_char_count(word: str) -> Dict[str, int]:
    char_counts: Dict[str, int] = {}
    for char in list(word):
        char_count = char_counts.get(char)
        char_counts[char] = char_count + 1 if char_count else 1
    return char_counts


def _get_permutations(word: str) -> list[str]:
    return _generate_permutations(word[1:], word[:1], [])


def _generate_permutations(remaining: str, prefix: str, permutations: list[str]) -> list[str]:
    if not remaining:
        permutations.append(prefix)
        return permutations

    remaining_post_pop = remaining[1:]
    popped_char = remaining[:1]

    for index in range(len(prefix) + 1):
        new_prefix = prefix[:index] + popped_char + prefix[index:]
        _generate_permutations(remaining_post_pop, new_prefix, permutations)

    return permutations


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


# 1.4 - Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase which is the same forwards and backwards. A permutation is an arrangement of letters.
# The palindrome does not need to be limited to dictionary words. Ignore casing and non-letter characters.
def is_a_palindrome(sentence: str) -> bool:
    char_counts = _generate_char_counts(sentence)
    
    odd_count = 0
    for count in char_counts.values():
        if odd_count > 1:
            return False
        if count % 2 == 1:
            odd_count += 1
        
    return True


def _generate_char_counts(sentence: str) -> Dict[str, int]:
    char_counts: Dict[str, int] = {}
    for char in list(sentence):
        lower_char = char.lower()
        if not _is_a_lower_character(lower_char):
            continue
        count = char_counts.get(lower_char)
        char_counts[lower_char] = count + 1 if count else 1
    
    return char_counts
        
def _is_a_lower_character(candidate: str) -> bool:
    a_val = ord('a')
    z_val = ord('z')
    candidate_val = ord(candidate)
    
    return a_val <= candidate_val and candidate_val <= z_val


# 1.5 - One Away: There are three types of edits that can be performed on strings, insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit(or zero edits) away.
def are_one_away(first: str, second: str) -> bool:
    if len(first) == len(second):
        return _check_one_edit_replace(first, second)
    
    elif len(first) + 1 == len(second):
        return _check_one_edit_insert(first, second)
    
    elif len(first) == len(second) + 1:
        return _check_one_edit_insert(second, first)
    
    else:
        return False
    
    
def _check_one_edit_replace(first: str, second: str) -> bool:
    edit_count = 0
    for index in range(len(first)):
        if edit_count > 1:
            return False
        if first[index:index+1] != second[index:index+1]:
            edit_count += 1
        
    return True


def _check_one_edit_insert(shorter: str, longer: str) -> bool:
    edit_count = 0
    shorter_index = 0
    longer_index = 0
    
    while shorter_index < len(shorter) and longer_index < len(longer):
        if edit_count > 1:
            return False
        elif shorter[shorter_index:shorter_index+1] != longer[longer_index:longer_index+1]:
            longer_index += 1
            edit_count += 1
        else:
            shorter_index += 1
            longer_index += 1
            
    return True
            
