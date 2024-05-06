import pytest

from string_permutations import permutations_from

@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param('ABC', {'CAB', 'BAC', 'ABC', 'ACB', 'BCA', 'CBA'}),
        pytest.param('one', {'oen', 'eno', 'eon', 'noe', 'one', 'neo'}),
    ]
)
def test_permutations_from_when_calculated_then_as_expected(word, expected): 
    actual = permutations_from(word)
    
    assert actual == expected
