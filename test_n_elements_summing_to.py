from n_elements_summing_to import pair_summing_to, triple_summing_to


def test_pair_summing_to_when_pair_exists_then_returned():
    numbers = [0, -1, 2, -3, 1]
    expected_pair = 1, -3
    
    actual_pair = pair_summing_to(-2, numbers)
    
    assert actual_pair == expected_pair


def test_triple_summing_to_when_triplet_exists_then_returned():
    numbers = [12, 3, 4, 1, 6, 9]
    expected_triple = 3, 1, 6
    
    actual_triple = triple_summing_to(10, numbers)
    
    assert actual_triple == expected_triple
