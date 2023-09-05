from optimize_and_solve.base_case_and_build import permutations


def test_permutations_when_calculated_then_has_expected_permutations():
    word = 'abc'
    expected = ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']
    
    actual = permutations(word)
    
    assert actual == expected