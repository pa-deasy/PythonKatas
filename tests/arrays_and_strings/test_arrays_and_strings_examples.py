from arrays_and_strings.arrays_and_strings_examples import is_permutation, is_unique, is_unique_no_datastructures, is_unique_no_datastructures_other, urlify


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