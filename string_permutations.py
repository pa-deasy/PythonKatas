def permutations_from(word: str, index: int = 0) -> set[str]:
    permutations_set = set()
    
    if index == len(word) - 1:
        return permutations_set
    
    for char_index in range(index, len(word)):
        permutation = _swap(word, index, char_index)
        permutations_set.add(permutation)
        permutations_set = permutations_set.union(permutations_from(permutation, index + 1))
        
    return permutations_set

        
def _swap(word: str, left_index: int, right_index: int):
    letters = list(word)
    letters[left_index], letters[right_index] = letters[right_index], letters[left_index]
    
    return ''.join(letters)
