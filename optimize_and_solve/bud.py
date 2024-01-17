from dataclasses import dataclass
from typing import Tuple


@dataclass
class EquationResult:
    a: int
    b: int
    c: int
    d: int


# O(N^4)
def a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_brute(limit: int) -> list[EquationResult]:
    matches: list[EquationResult] = []
    
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                for d in range(1, limit):
                    if a**3 + b**3 == c**3 + d**3:
                        matches.append(EquationResult(a=a, b=b, c=c, d=d))
                        
    return matches


# O(N^3)
def a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_unnecessary(limit: int) -> list[EquationResult]:
    matches: list[EquationResult] = []
    
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                
                potential_d = round(a**3 + b**3 - c**3)
                if potential_d <= 0:
                    continue
                d = round(potential_d**(1/3))
                if a**3 + b**3 == c**3 + d**3 and d > 0 and d <= limit:
                    matches.append(EquationResult(a=a, b=b, c=c, d=d))
                    continue
                        
    return matches


# O(N^2)
def a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_duplicated(limit: int) -> list[EquationResult]:
    matches: list[EquationResult] = []
    cache: dict[int, list[Tuple[int, int]]] = {}
    
    for c in range(1, limit):
        for d in range(1, limit):
            result = c**3 + d**3
            existing_result = cache.get(result)
            cache[result] = existing_result + [(c, d)] if existing_result else [(c, d)]
            
    for pairs in cache.values():
        for (c, d) in pairs:
            matches.append(EquationResult(a=c, b=d, c=c, d=d))
                
                        
    return matches