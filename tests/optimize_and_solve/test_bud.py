import pytest
from optimize_and_solve.bud import a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_brute, a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_duplicated, a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_unnecessary


def test_a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_brute_when_calculated_then_returns_expected():
    result = a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_brute(10)
    
    assert len(result) == 153
    

def test_a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_unnecessary_when_calculated_then_returns_expected():
    result = a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_unnecessary(10)
    
    assert len(result) == 153
    

@pytest.mark.skip(reason='not sure what this is supposed to do')
def test_a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_duplicated_when_calculated_then_returns_expected():
    result = a_cubed_plus_b_cuded_equals_c_cubed_plus_d_cubed_duplicated(10)
    
    assert len(result) == 153