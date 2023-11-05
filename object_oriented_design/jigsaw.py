from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from linked_lists.linked_lists_examples import LinkedList


class Orientation(Enum):
    LEFT = 'left'
    TOP = 'top'
    RIGHT = 'right'
    BOTTOM = 'bottom'
    
    def get_opposite(self) -> 'Orientation':
        if self == Orientation.LEFT:
            return Orientation.RIGHT
        elif self == Orientation.RIGHT:
            return Orientation.LEFT
        elif self == Orientation.TOP:
            return Orientation.BOTTOM
        elif self == Orientation.BOTTOM:
            return Orientation.TOP
        else:
            return None


class Shape(Enum):
    OUTER = 'outer'
    INNER = 'inner'
    FLAT = 'flat'
    
    def get_opposite(self) -> 'Shape':
        if self == Shape.OUTER:
            return Shape.INNER
        elif self == Shape.INNER:
            return Shape.OUTER
        else:
            None
            

@dataclass
class Edge:
    orientation: Orientation
    shape: Shape
    parent_piece: 'Piece'
    
    def fits_with(self, other: 'Edge') -> bool:
        return False
    

class Piece:
    edges: Dict[Orientation, Edge]
    
    def rotate_edges(self, rotations: int) -> None:
        return None
    
    def set_edge_as_orientation(self, edge: Edge, orientation: Orientation) -> None:
        other = self.edges.get(orientation)
        opposite = other.orientation.get_opposite()
        other.orientation = opposite
        self.edges[opposite] = other
        self.edges[orientation] = edge
    

class Puzzle:
    pieces: LinkedList[Piece]
    solution: List[List[Piece]]
    size: int
    
    def __init__(self, pieces: List[Piece], solution: List[List[Piece]], size: int) -> None:
        self.pieces = pieces
        self.solution = solution
        self.size = size
        
    def solve(self) -> List[List[Piece]]:
        corner_pieces = LinkedList()
        border_pieces = LinkedList()
        inside_pieces = LinkedList()
        self._group_pieces(corner_pieces, border_pieces, inside_pieces)
        
        for row in range(self.size):
            for column in range(self.size):
                pieces_to_search = self._get_pieces_to_search(corner_pieces, border_pieces, inside_pieces)
                self._fit_next_edge(pieces_to_search, row, column)

        return self.solution
        
    def _set_edge_in_solution(self, pieces: LinkedList, edge: Edge, row: int, column: int, orientation: Orientation) -> None:
        piece = edge.parent_piece
        piece.set_edge_as_orientation(edge, orientation)
        pieces.delete_node(piece)
        self.solution[row][column] = piece
        
    def _orient_top_left_corner(self, piece: Piece) -> None:
        return
    
    def _get_matching_edge(self, edge_to_match: Edge, pieces_to_search: LinkedList) -> Edge:
        return Edge()
        
    def _fit_next_edge(self, pieces_to_search: LinkedList, row: int, column: int) -> None:
        if row == 0 and column == 0:
            p: Piece = pieces_to_search.remove_first().value
            self._orient_top_left_corner(p)
            self.solution[0][0] = p     
        else:
            piece_to_match = self.solution[row - 1][0] if column == 0 else self.solution[row][column - 1]
            orientation_to_match = Orientation.BOTTOM if column == 0 else Orientation.BOTTOM
            edge_to_match = piece_to_match.edges.get(orientation_to_match)
            
            edge = self._get_matching_edge(edge_to_match, pieces_to_search)
            if edge == None:
                raise Exception("Can't solve")
            
            orientation = orientation_to_match.get_opposite()
            self._set_edge_in_solution(pieces_to_search, edge, row, column, orientation)
            
    def _group_pieces(corner_pieces: LinkedList, border_pieces: LinkedList, inside_pieces: LinkedList) -> None:
        return
    
    def _get_pieces_to_search(corner_pieces: LinkedList, border_pieces: LinkedList, inside_pieces: LinkedList, row: int, column: int) -> LinkedList:
        return LinkedList()
    