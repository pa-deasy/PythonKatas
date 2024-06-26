import pytest
from big_o.big_o_examples import all_fib, all_fib_optomized, copy_numbers, div, factorial, fib, foo_sum_product, intersection, is_prime, mod, permutation, power, powers_of_2, print_pairs, print_unordered_pairs, print_unordered_pairs_by_4, print_unordered_pairs_less_than, product, reverse, sorted_strings, sqrt, sqrt_linear, sum_balanced_nodes, sum_digits
from big_o.node import Node


def test_foo_sum_product_when_calulated_then_as_expected():
    numbers = [1, 3, 2, 2]
    expected_sum = 8
    expected_product = 12
    expected = expected_sum, expected_product
    
    actual = foo_sum_product(numbers)
    
    assert actual == expected
    

def test_print_pairs_when_retrieved_then_as_expected():
    numbers = [1, 5, 7]
    expected = [(1, 1), (1, 5), (1, 7), (5, 1), (5, 5), (5, 7), (7, 1), (7, 5), (7, 7)]
    
    actual = print_pairs(numbers)
     
    assert actual == expected
    

def test_print_unordered_pairs_when_retrieved_then_as_expected():
    numbers = [1, 5, 7]
    expected = [(1, 5), (1, 7), (5, 7)]
    
    actual = print_unordered_pairs(numbers)
     
    assert actual == expected
    

def test_print_unordered_pairs_less_than_when_retrieved_then_as_expected():
    numbers_a = [1, 5, 7]
    numbers_b = [9, 3]
    expected = [(1, 9), (1, 3), (5, 9), (7, 9)]
    
    actual = print_unordered_pairs_less_than(numbers_a, numbers_b)
     
    assert actual == expected
    
    
def test_print_unordered_pairs_by_4_when_retrieved_then_as_expected():
    numbers_a = [1, 5]
    numbers_b = [9]
    expected = [(1, 9), (1, 9), (1, 9), (1, 9), (5, 9), (5, 9), (5, 9),(5, 9)]
    
    actual = print_unordered_pairs_by_4(numbers_a, numbers_b)
     
    assert actual == expected
    

def test_reverse_when_reversed_then_in_correct_order():
    numbers = [1, 5, 7, 9]
    expected = [9, 7, 5, 1]
    
    actual = reverse(numbers)
    
    assert actual == expected
    
    
def test_sum_balanced_nodes_when_summed_then_correct_value():
    node_b = Node(value=1, left=None, right=None)
    node_c = Node(value=7, left=None, right=None)
    node_a = Node(value=3, left=node_b, right=node_c)
    
    
    expected = 11
    
    actual = sum_balanced_nodes(node_a)
    
    assert actual == expected
    
    
def test_is_prime_when_predicted_then_is_expected():
    assert is_prime(13) is True
    assert is_prime(97) is True
    assert is_prime(9) is False
    
    
def test_factorial_when_calculated_then_is_expected():
    assert factorial(5) == 120
    

def test_permutation_when_calculated_then_has_expected_permutations():
    word = 'abc'
    expected = {'cba', 'acb', 'abc', 'bca', 'cab', 'bac'}
    
    actual = permutation(word)
    
    assert actual == expected
    
    
def test_fib_when_calculated_then_is_expected_number():
    expected = 8
    actual = fib(6)
    
    assert actual == expected
    
    
def test_all_fibs_when_calculated_then_all_numbers_as_expected():
    expected = [0, 1, 1, 2, 3, 5, 8]
    
    actual = all_fib(6)
    
    assert actual == expected


def test_all_fibs_optomized_when_calculated_then_all_numbers_as_expected():
    expected = [0, 1, 1, 2, 3, 5, 8]
    
    actual = all_fib_optomized(6)
    
    assert actual == expected
    
    
def test_powers_of_2_when_calculated_then_returns_expected_numbers():
    expected = {1, 2, 4}
    
    actual = powers_of_2(4)
    
    assert actual == expected
    

def test_product_when_calculated_then_result_as_expected():
    assert product(2, 3) == 6
    

def test_power_when_calculated_then_result_as_expected():
    assert power(2, 3) == 8
    
    
def test_mod_when_modded_then_result_as_expected():
    assert mod(33, 10) == 3
    

def test_div_when_divided_then_result_as_expected():
    assert div(30, 10) == 3
    
    
def test_sqrt_when_calculated_then_sqrt_as_expected():
    assert sqrt(25) == 5
    

def test_sqrt_linear_when_calculated_then_sqrt_as_expected():
    assert sqrt_linear(25) == 5
    

def test_copy_numbers_when_copied_then_new_numbers_as_expected():
    numbers = [2, 4, 33, 25]
    
    copied = copy_numbers(numbers)
    
    assert copied == numbers
    

def test_sum_digits_when_summed_then_sum_as_expected():
    assert sum_digits(24) == 6
    assert sum_digits(732) == 12
    

pytest.mark.skip(reason='No idea what this is supposed to really do')
def test_sorted_strings_when_sorted_then_as_expected():
    expected = []
    
    actual = sorted_strings(4)
    
    assert actual == expected
    
    
def test_intersection_when_obtained_then_matches_expected_intersection():
    expected = [5, 9]
    a = [10, 5, 1, 9, 7]
    b = [3, 2, 4, 6, 8, 5, 11, 9]
    
    actual = intersection(a, b)
    
    assert actual == expected