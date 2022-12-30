import pytest

from theft import StealableItem, calculate_maximum_profit


@pytest.fixture
def items_a():
    stereo = StealableItem(name='stereo', value=3000, weight=4)
    laptop = StealableItem(name='laptop', value=2000, weight=3)
    guitar = StealableItem(name='guitar', value=1500, weight=1)
    
    return [stereo, laptop, guitar]


@pytest.fixture
def items_b():
    stereo = StealableItem(name='stereo', value=3000, weight=4)
    laptop = StealableItem(name='laptop', value=2000, weight=3)
    guitar = StealableItem(name='guitar', value=1500, weight=1)
    iphone = StealableItem(name='iphone', value=2000, weight=1)
    
    return [stereo, laptop, guitar, iphone]
    

def test_calculate_maximum_profit_when_item_set_a_then_as_expected(items_a):
    bag_size = 4
    profit = calculate_maximum_profit(items_a, bag_size)
    
    assert profit == 3500
    
    
def test_calculate_maximum_profit_when_item_set_b_then_as_expected(items_b):
    bag_size = 4
    profit = calculate_maximum_profit(items_b, bag_size)
    
    assert profit == 4000