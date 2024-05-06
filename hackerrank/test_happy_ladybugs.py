import pytest

from happy_ladybugs import are_ladybugs_happy

@pytest.mark.parametrize(
    "ladybugs,expected",
    [
        pytest.param('YYR_B_BR', 'YES'),
        pytest.param('RBY_YBR', 'YES'),
        pytest.param('X_Y__X', 'NO'),
        pytest.param('__', 'YES'),
        pytest.param('B_RRBR', 'YES'),
        pytest.param('AABBC', 'NO'),
        pytest.param('AABBC_C', 'YES'),
        pytest.param('_', 'YES'),
        pytest.param('DD__FQ_QQF', 'YES'),
        pytest.param('AABCBC', 'NO'),
        pytest.param('RBRB', 'NO'),
        pytest.param('RRRR', 'YES'),
        pytest.param('BBB', 'YES'),
        pytest.param('BBB_', 'YES')
    ]
)
def test_are_ladybugs_happy_when_ladybugs_arranged_then_returns_expected_result(ladybugs, expected):
    actual = are_ladybugs_happy(ladybugs)
    
    assert actual == expected
