import pytest

from element_frequency import k_most_frequency


@pytest.mark.parametrize(
    "k,expected",
    [
        pytest.param(4, ['three', 'two', 'one', 'another one']),
        pytest.param(2, ['three', 'two']),
    ]
)
def test_k_most_frequency_when_calculated_then_as_expected(k, expected):
    elements = ['one', 'two', 'three', 'two', 'three', 'three', 'another one']
    
    actual = k_most_frequency(k, elements)
    
    assert actual == expected
