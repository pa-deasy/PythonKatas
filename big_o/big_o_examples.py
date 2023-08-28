# O(N) - iterating the array twice doesn't matter
from typing import Optional
from big_o.node import Node


def foo_sum_product(numbers: list[int]) -> tuple[int, int]:
    sum = 0
    product = 1
    for number in numbers:
        sum += number
    for number in numbers:
        product *= number
    
    return sum, product


# O(N^2) - inner loop has O(N) interations and is called N times
def print_pairs(numbers: list[int]) -> tuple[int, int]:
    pairs: list[tuple[int, int]] = []
    for number_left in numbers:
        for number_right in numbers:
            pairs.append((number_left, number_right))
    
    return pairs


# O(N^2) - N^2/2 amount of work
def print_unordered_pairs(numbers: list[int]) -> tuple[int, int]:
    pairs: list[tuple[int, int]] = []
    
    for index_left in range(len(numbers) - 1):
        for index_right in range(index_left + 1, len(numbers)):
            pairs.append((numbers[index_left], numbers[index_right]))
    
    return pairs


# O(ab) - two differect inputs of a and b being iterated
def print_unordered_pairs_less_than(numbers_a: list[int], numbers_b: list[int]) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    
    for number_a in numbers_a:
        for number_b in numbers_b:
            if number_a < number_b:
                pairs.append((number_a, number_b))
                
    return pairs
    

# O(ab) - nothing has changed since the last example except for the iteration of 4 which is constant
def print_unordered_pairs_by_4(numbers_a: list[int], numbers_b: list[int]) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    
    for number_a in numbers_a:
        for number_b in numbers_b:
            for index in range(4):
                pairs.append((number_a, number_b))
                
    return pairs


# O(N) - the fact that it iterates half of the list does not impact the big O time
def reverse(numbers: list[int]) -> list[int]:
    for left_index in range(round(len(numbers)/2)):
        right_index = len(numbers) - left_index - 1
        temp = numbers[left_index]
        numbers[left_index] = numbers[right_index]
        numbers[right_index] = temp
        
    return numbers
                

# O(N) - The code touches each node in the tree once and does a constant time amount of work, O(2 ^ log N) which is the same as O(N)
def sum_balanced_nodes(node: Optional[Node]):
    if node is None:
        return 0
    
    return sum_balanced_nodes(node.left) + node.value + sum_balanced_nodes(node.right)


# O(sqrt n) - work is constant inside the while loop and the worst case number of iterations of the loop is square root of n
def is_prime(n: int) -> bool:
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x += 1
    
    return True


# O(N) - simple recursion through n - 1 to 1
def factorial(n: int) -> int:
    if n < 0:
        return - 1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

# O(N * N!) - O(N!) calls to _calculate_permutations each of which takes O(N) time
def permutation(word: str) -> set[str]:
    return _calculate_permutations(word, '', set())
    
    
def _calculate_permutations(word: str, prefix: str, permutations: set[str]) -> set[str]:
    if not word:
        permutations.add(prefix)
        return permutations
    
    for index in range(len(word)):
        rem = word[0: index] + word[index + 1:]
        new_permutations = _calculate_permutations(rem, prefix + word[index], permutations)
        permutations = permutations.union(new_permutations)
        
    return permutations


# O(2^N) - multiple recursive calls
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# O(2^N) - similar to last example but because the N is changing each iteration the result is O(2^N) and not O(N 2^N)
def all_fib(n: int) -> list[int]:
    all_fibs: list[int] = []
    for index in range(n + 1):
        all_fibs.append(fib(index))
        
    return all_fibs


# O(N) - takes a constant amount of time since the value at n is being cached
def all_fib_optomized(n: int) -> list[int]:
    memo: list[Optional[int]] = [None for x in range(0, n + 1)]
    all_fibs: list[int] = []
    for index in range(n + 1):
        all_fibs.append(_fib_optomized(index, memo))
        
    return all_fibs
    

def _fib_optomized(n: int, memo:list[int]) -> int:
    if memo[n]:
        return memo[int]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
    

# O(log N) - the number of times we can divide N by 2 until 1 is reached
def powers_of_2(n: int, powers: set[int] = set()) -> set[int]:
    if n < 1:
        powers.add(0)
        return powers
    elif n == 1:
        powers.add(1)
        return powers
    previous_powers = powers_of_2(n / 2, powers)
    current = list(previous_powers)[-1] * 2
    previous_powers.add(current)
    
    return previous_powers
    