import pytest

from number_to_word import NumberAsWord


@pytest.mark.parametrize(
    "number, expected",
    [
        pytest.param(1, 'one'),
        pytest.param(10, 'ten'),
        pytest.param(20, 'twenty'),
        pytest.param(28, 'twenty eight'),
        pytest.param(80, 'eighty'),
        pytest.param(53, 'fifty three'),
    ]
)
def test_number_as_word_when_created_then_value_as_expected(number, expected):
    number_as_word = NumberAsWord(number)
    assert number_as_word.value == expected
