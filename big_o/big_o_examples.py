# O(N) - iterating the array twice doesn't matter
import math
import string
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


# O(b) - just iterates through b
def product(a: int, b: int) -> int:
    sum = 0
    for index in range(b):
        sum += a
        
    return sum


# O(b) - resursive code iterates through b
def power(a: int, b:int) -> int:
    if b < 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, b - 1)
    

# O(1) - constant amount of work
def mod(a: int, b: int) -> int:
    if b <= 0:
        return -1
    div = int(a / b)
    return a - div * b


# O(a/b) - interates a/b times
def div(a: int, b: int) -> int:
    count = 0
    sum = b
    while sum <= a:
        count += 1
        sum += b
    
    return count


# O(N log N) - essentially doing a binary search
def sqrt(n: int) -> int:
    return _sqrt_finder(n, 1, n)
    
    
def _sqrt_finder(n: int, min: int, max: int) -> int:
    if max < min:
        return -1
    
    guess = round((min + max) / 2)
    if guess * guess == n:
        return guess
    elif guess * guess < n:
        return _sqrt_finder(n, guess + 1, max)
    else:
        return _sqrt_finder(n, min, guess - 1)
    

# O(sqrt N) - iterates through the loop until the sqrt is hit or passed
def sqrt_linear(n: int):
    guess = 1
    while guess * guess <= n:
        if guess * guess == n:
            return guess
        guess += 1
        
    return -1


# O(N^2) - total time is sum of 1 through N
def copy_numbers(numbers: list[int]) -> list[int]:
    copy: list[int] = []
    for n in numbers:
        copy = _append_to_new(copy, n)
    
    return copy
    
def _append_to_new(numbers: list[int], number: int) -> list[int]:
    new: list[int] = []
    
    for n in numbers:
        new.append(n)
        
    new.append(number)
    return new


# O(log N) - number of digit in N. A number with d digits can have value up to 10^d .
def sum_digits(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n = math.floor(n / 10)
        
    return sum


# O(kc^k) - k is len str and c is num of chars in alphabet. Takes O(c^k) to generate each str. To then check each of these str is sorted takes O(k)
def sorted_strings(remaining: int) -> list[str]:
    return _generate_sorted_strings(remaining, '', [])


def _generate_sorted_strings(remaining: int, prefix: str, sorted_strings: list[str]) -> list[str]:
    alphabet = list(string.ascii_lowercase)
    if remaining == 0:
        if _is_in_order(prefix):
            sorted_strings.append(prefix)
            return sorted_strings
    else:
        for char in alphabet:
            return sorted_strings + _generate_sorted_strings(remaining - 1, prefix + char, sorted_strings)
        
        
def _is_in_order(word: str) -> bool:
    is_in_order = True
    chars = list(word)
    for index in range(1, len(chars)):
        if chars[index - 1] > chars[index]:
            is_in_order = False
    
    return is_in_order


# O(b log b + a log b) - Mergesort is b log b plus iterate over a for a binary search of log b
def intersection(a: list[int], b: list[int]) -> list[int]:
    intersects: list[int] = []
    sorted_b = _mergesort(b)
    
    for n in a:
        if _binary_search(sorted_b, n) >= 0:
            intersects.append(n)
            
    return intersects
    

def _mergesort(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers
    
    pivot = round(len(numbers) / 2)
    left = numbers[:pivot]
    right = numbers[pivot:]
    
    return _merge(_mergesort(left), _mergesort(right))
    


def _merge(left: list[int], right: list[int]) -> list[int]:
    merged: list[int] = []
    
    while left:
        if right and left[0] > right[0]:
            merged.append(right.pop(0))
        else:
            merged.append(left.pop(0))
            
    if right:
        merged += right
        
    return merged


def _binary_search(numbers: list[int], target: int) -> int:
    low = 0
    high = len(numbers) - 1
    
    while low <= high:
        mid = round((low + high) / 2)
        guess = numbers[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1