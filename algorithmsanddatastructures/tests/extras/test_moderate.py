import pytest
from extras.moderate import Book, Line, Move, Page, Player, Point, TicTacToe, find_point_of_intersection, swap_numbers


@pytest.mark.parametrize(
    'numbers,first_index,second_index,expected',
    [
        pytest.param([1, 2, 3, 4, 5], 0, 4, [5, 2, 3, 4, 1]),
        pytest.param([1, -2, 3, 4, 5], 1, 3, [1, 4, 3, -2, 5])
    ]
)
def test_swap_numbers_when_swapped_then_numbers_array_as_expected(numbers, first_index, second_index, expected):
    swap_numbers(numbers, first_index, second_index)
    
    assert numbers == expected
    
    
@pytest.fixture
def book():
    return Book(
        pages=[
            Page(number=1, content='Harry ran down the stairs, today was the day he returned to Hogwarts.'),
            Page(number=2, content='He mused the idea of a new broom over in his head, would be nice.'),
            Page(number=3, content='Professor Snape never really did like Harry or so he thought.'),
            Page(number=4, content='The last day of Hogwarts was a bitsweet one.'),
        ]
    )
    
def test_occurrences_of_when_calculated_then_returns_correct_count(book):
    assert book.count_occurrences_of('he') == 3
    assert book.count_occurrences_of('harry') == 2
    
    
def test_is_won_when_game_is_won_for_player_then_returns_true():
    layout = [
        [Player.O, Player.X, None],
        [None, Player.X, None],
        [Player.O, Player.X, None],
    ]
    
    tictactoe = TicTacToe(layout=layout)
    
    assert tictactoe.is_won(Move(row=2, column=1, player=Player.X)) is True
    
    
def test_is_won_when_game_is_won_for_other_player_then_returns_false():
    layout = [
        [Player.O, Player.X, None],
        [None, Player.X, None],
        [Player.O, Player.X, None],
    ]
    
    tictactoe = TicTacToe(layout=layout)
    
    assert tictactoe.is_won(Move(row=2, column=0, player=Player.O)) is False
    
    
def test_is_won_when_game_is_not_won_for_player_then_returns_false():
    layout = [
        [Player.O, Player.X, None],
        [None, Player.X, None],
        [Player.O, Player.O, Player.X],
    ]
    
    tictactoe = TicTacToe(layout=layout)
    
    assert tictactoe.is_won(Move(row=2, column=1, player=Player.X)) is False