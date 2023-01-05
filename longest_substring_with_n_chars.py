def longest_substring_of(char_limit: int, word: str) -> str:
    longest_substring: list[str] = []
    substring: list[str] = []
    
    for char in list(word):
        substring.append(char)
        unique_chars = set(substring)
        
        if len(unique_chars) > char_limit:
            substring = _reduce_unique_chars(char_limit, substring)
        
        if len(substring) > len(longest_substring):
            longest_substring = substring.copy()
            
        
    return ''.join(longest_substring)


def _reduce_unique_chars(char_limit: int, substring: list[str]) -> list[str]:
    unqiue_chars = set()
    new_substring: list[str] = []
    
    while(substring):
        char = substring.pop()
        unqiue_chars.add(char)
        
        if len(unqiue_chars) > char_limit:
            break
        
        new_substring = [char] + new_substring
        
    return new_substring
