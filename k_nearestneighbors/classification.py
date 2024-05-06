from dataclasses import dataclass
from enum import Enum
from math import sqrt


class FruitType(Enum):
    GRAPEFRUIT = 1
    ORANGE = 2
    UNKNOWN = 3
    

@dataclass
class Fruit():
    size: int
    redness: int
    fruit_type: FruitType
    

@dataclass
class FruitSimilarity():
    fruit_type: FruitType
    similarity: float
    

def grapefruit_or_orange(fruits: list[Fruit], unknown_fruit: Fruit) -> Fruit:
    fruit_similarities = [FruitSimilarity(fruit_type=f.fruit_type, similarity=_fruit_similarity(unknown_fruit, f)) for f in fruits]
    fruit_similarities.sort(key=lambda f: f.similarity)
    closest_3_fruits = fruit_similarities[:3]
    
    count_closest_oranges = [f for f in closest_3_fruits if f.fruit_type == FruitType.ORANGE]
    count_closest_grapefruits = [f for f in closest_3_fruits if f.fruit_type == FruitType.GRAPEFRUIT]
    
    if (count_closest_grapefruits > count_closest_oranges):
        unknown_fruit.fruit_type = FruitType.GRAPEFRUIT
    else:
        unknown_fruit.fruit_type = FruitType.ORANGE
        
    return unknown_fruit


def _fruit_similarity(fruit_a: Fruit, fruit_b: Fruit):
    return sqrt(pow((fruit_a.size - fruit_b.size), 2) + pow((fruit_a.redness - fruit_b.redness), 2))
