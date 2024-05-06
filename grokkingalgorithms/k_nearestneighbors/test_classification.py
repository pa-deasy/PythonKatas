import pytest

from classification import Fruit, FruitType, grapefruit_or_orange

@pytest.fixture
def fruits():
    orange_1 = Fruit(size=2,redness=2,fruit_type=FruitType.ORANGE)
    orange_2 = Fruit(size=2,redness=1,fruit_type=FruitType.ORANGE)
    orange_3 = Fruit(size=1,redness=1,fruit_type=FruitType.ORANGE)
    grapefruit_1 = Fruit(size=4,redness=4,fruit_type=FruitType.GRAPEFRUIT)
    grapefruit_2 = Fruit(size=5,redness=5,fruit_type=FruitType.GRAPEFRUIT)
    grapefruit_3 = Fruit(size=6,redness=7,fruit_type=FruitType.GRAPEFRUIT)
    
    return [orange_1, orange_2, orange_3, grapefruit_1, grapefruit_2, grapefruit_3]


def test_grapefruit_or_orange_when_grapefruit_then_returns_grapefruit(fruits):
    unknown_fruit = Fruit(size=5,redness=8,fruit_type=FruitType.UNKNOWN)
    
    known_fruit = grapefruit_or_orange(fruits, unknown_fruit)
    
    assert known_fruit.fruit_type == FruitType.GRAPEFRUIT
    

def test_grapefruit_or_orange_when_orange_then_returns_orange(fruits):
    unknown_fruit = Fruit(size=3,redness=2,fruit_type=FruitType.UNKNOWN)
    
    known_fruit = grapefruit_or_orange(fruits, unknown_fruit)
    
    assert known_fruit.fruit_type == FruitType.ORANGE
