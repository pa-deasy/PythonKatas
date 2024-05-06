import pytest

from save_the_prisoner import save_the_prisoner


@pytest.mark.parametrize(
    "prisoner_count,candy_count,starting_chair,expected",
    [
        pytest.param(4, 6, 2, 3),
        pytest.param(5, 2, 1, 2),
        pytest.param(5, 2, 2, 3),
        pytest.param(7, 19, 2, 6),
        pytest.param(3, 7, 3, 3),
    ]
)
def test_save_the_prisoner_when_saved_then_as_expected(prisoner_count, candy_count, starting_chair, expected):
    actual = save_the_prisoner(prisoner_count, candy_count, starting_chair)
    
    assert actual == expected
 