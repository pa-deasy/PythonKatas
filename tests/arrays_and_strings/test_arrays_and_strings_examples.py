from arrays_and_strings.arrays_and_strings_examples import are_one_away, compress, is_a_palindrome, is_permutation, is_unique, is_unique_no_datastructures, is_unique_no_datastructures_other, propagate_zeros, rotate, urlify
import pytest


def test_is_unique_when_unique_then_returns_true():
    assert is_unique('abcgsdn') is True


def test_is_unique_when_not_unique_then_returns_false():
    assert is_unique('abcdfck') is False


def test_is_unique_no_datastructures_when_unique_then_returns_true():
    assert is_unique_no_datastructures('abcgsdn') is True


def test_is_unique_no_datastructures_when_not_unique_then_returns_false():
    assert is_unique_no_datastructures('abcdfck') is False


def test_is_unique_no_datastructures_other_when_unique_then_returns_true():
    assert is_unique_no_datastructures_other('abcgsdn') is True


def test_is_unique_no_datastructures_other_when_not_unique_then_returns_false():
    assert is_unique_no_datastructures_other('abcdfck') is False


def test_is_permutation_when_checked_then_results_is_as_expected():
    assert is_permutation('abc', 'bac') is True
    assert is_permutation('abcdef', 'zb') is False


def test_urlify_when_converted_then_matches_expected():
    input = ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ',  'S', 'm', 'i', 't', 'h', ' ', ' ', ' ']
    true_length = 13
    expected = ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h']
    
    actual = urlify(input, true_length)
    
    assert actual == expected
    

@pytest.mark.parametrize(
    "sentence, expected",
    [
        pytest.param('Tact Cao', True),
        pytest.param('Ci-v ic', True),
        pytest.param('gikgs', False)
    ]
)
def test_is_a_palindrome_when_sentence_checked_then_result_is_as_expected(sentence, expected):
    actual = is_a_palindrome(sentence)
    
    assert actual == expected
    
    
@pytest.mark.parametrize(
    "target,candidate,expected",
    [
        pytest.param('pale', 'ple', True),
        pytest.param('pales', 'pale', True),
        pytest.param('pale', 'pales', True),
        pytest.param('pale', 'bale', True),
        pytest.param('pale', 'bake', False),
        pytest.param('palers', 'pale', False),
        pytest.param('palers', 'piler', False),
    ]
)
def test_are_one_away_when_words_compared_then_returns_expected_result(target, candidate, expected):
    actual = are_one_away(target, candidate)
    
    assert actual == expected
    

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('aabcccccaaa', 'a2b1c5a3'),
        pytest.param('aabccccca', 'a2b1c5a1'),
        pytest.param('abcde', 'abcde')
    ]
)
def test_compress_when_input_is_compressed_then_output_is_as_expected(input, expected):
    actual = compress(input)
    
    assert actual == expected
    
    
def test_rotate_when_given_3_x_3_matrix_rotated_then_result_is_as_expected():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    
    actual = rotate(matrix)
    
    assert actual == expected
    

def test_rotate_when_given_4_x_4_matrix_rotated_then_result_is_as_expected():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    
    expected = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]
    
    actual = rotate(matrix)
    
    assert actual == expected
    
    
def test_propegate_zeros_when_zeros_exist_then_rows_and_columns_are_updated():
    matrix = [
        [1, 2, 0, 4],
        [5, 6, 7, 8],
        [9, 0, 11, 12],
        [13, 14, 15, 16],
    ]
    
    expected = [
        [0, 0, 0, 0],
        [5, 0, 0, 8],
        [0, 0, 0, 0],
        [13, 0, 0, 16],
    ]
    
    actual = propagate_zeros(matrix)
    
    assert actual == expected
