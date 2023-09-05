from optimize_and_solve.diy import find_all_permutations


def test_find_all_permutations_when_found_then_all_results_as_expected():
    s = 'abbc'
    b = 'cbabadcbbabbcbabaabccbabc'
    expected = ['cbab', 'cbba', 'abbc', 'bcba', 'cbab', 'cbab', 'babc']
    
    actual = find_all_permutations(s, b)
    
    assert actual == expected


