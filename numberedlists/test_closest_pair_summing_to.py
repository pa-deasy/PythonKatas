import pytest

from closest_pair_summing_to import closest_pair_to_sum


def test_closest_pair_to_sum_when_0_then_returns_closest_pair():
    numbers = [1, 60, -10, 70, -80, 85]
    closest_first, closes_second = closest_pair_to_sum(numbers, 0)
    
    assert closest_first == -80
    assert closes_second == 85
    

def test_closest_pair_to_sum_when_9_then_returns_closest_pair():
    numbers = [1, -21, -8, 29, -1 , 85]
    closest_first, closes_second = closest_pair_to_sum(numbers, 9)
    
    assert closest_first == -21
    assert closes_second == 29
