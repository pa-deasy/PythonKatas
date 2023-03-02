import pytest

from matrix_rotation import Matrix


@pytest.fixture
def three_x_three():
    cells = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    return Matrix(cells=cells)


@pytest.fixture
def four_x_four():
    cells = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    return Matrix(cells=cells)
   
    
@pytest.fixture
def six_x_six():
    cells = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36]
    ]
    return Matrix(cells=cells)
    

def test_rotate_90_anti_clockwise_when_3_x_3_then_as_expected(three_x_three):
    expected_cells = [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ]
    
    three_x_three.rotate_90_anti_clockwise()
    
    assert three_x_three.cells == expected_cells
    

def test_rotate_90_anti_clockwise_when_4_x_4_then_as_expected(four_x_four):
    expected_cells = [
        [4, 8, 12, 16],
        [3, 7, 11, 15],
        [2, 6, 10, 14],
        [1, 5, 9, 13]
    ]
    
    four_x_four.rotate_90_anti_clockwise()
    
    assert four_x_four.cells == expected_cells
    

def test_rotate_90_anti_clockwise_when_6_x_6_then_as_expected(six_x_six):
    expected_cells = [
        [6, 12, 18, 24, 30, 36],
        [5, 11, 17, 23, 29, 35],
        [4, 10, 16, 22, 28, 34],
        [3, 9, 15, 21, 27, 33],
        [2, 8, 14, 20, 26, 32],
        [1, 7, 13, 19, 25, 31]
    ]
    
    six_x_six.rotate_90_anti_clockwise()
    
    assert six_x_six.cells == expected_cells
