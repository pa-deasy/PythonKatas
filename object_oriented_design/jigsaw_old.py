from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

from stacks_and_queues.stacks_and_queues_examples import Stack


# 7.6 - Jigsaw: Implement an NxN jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle.
# You can assume you have a fitsWith() method which, when passes two puzzle edges, returns true if the two edges belong together.
class Orientation(Enum):
    LEFT = 'left'
    TOP = 'top'
    RIGHT = 'right'
    BOTTOM = 'bottom'
    
    
class Shape(Enum):
    INNER = 'inner'
    OUTTER = 'outter'
    FLAT = 'flat'


class Edge:
    id: int
    shape: Shape
    piece_id: int
    
    def fits_with(other: 'Edge') -> bool:
        return True
    
 
@dataclass
class Piece:
    id: int
    size: int
    edges: Dict[Orientation, Edge]
    image: str


class Jigsaw:
    pieces = Stack[Piece]
    solution: List[List[Piece]]
    
                