# Given a smaller string s and a bigger string b, design an algorithm to find all perumations of the shorter string within the long one.

import copy
from typing import Dict


def find_all_permutations(s: str, b: str) -> list[str]:
    permutations: list[str] = []
    s_char_counts = _generate_char_counts(s)
    
    for index in range (0, len(b) - len(s) + 1):
        sample = b[index: index + len(s)]
        if _has_permutation_match(s_char_counts, sample):
            permutations.append(sample)
            
    return permutations


def _has_permutation_match(s_char_counts: Dict[str, int], sample: str) -> bool:
    s_char_counts_copy = copy.deepcopy(s_char_counts)
    for char in list(sample):
        s_char_count = s_char_counts_copy.get(char)
        if not s_char_count or s_char_count == 0:
            return False
        elif s_char_count > 0:
            s_char_counts_copy[char] = s_char_count - 1
            
    return True
            

def _generate_char_counts(s: str) -> Dict[str, int]:
    char_counts: Dict[str, int] = {}
    for char in list(s):
        char_count = char_counts.get(char)
        char_counts[char] = char_count + 1 if char_count else 1
    
    return char_counts
