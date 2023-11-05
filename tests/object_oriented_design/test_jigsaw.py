from typing import Dict
from object_oriented_design.jigsaw import Edge, Orientation, Piece, Shape


def test_orientation_when_opposite_retrieved_then_matches_expected():
    orientation = Orientation.LEFT
    opposite = orientation.get_opposite()
    
    assert opposite == Orientation.RIGHT
    

def test_shape_when_opposite_retrieved_then_matches_expected():
    shape = Shape.INNER
    opposite = shape.get_opposite()
    
    assert opposite == Shape.OUTER
    
    
def test_piece_when_edge_set_as_orientation_then_edges_are_swapped_correctly():
    piece = Piece
    left_edge = Edge(orientation=Orientation.LEFT, shape=Shape.OUTER, parent_piece=piece)
    top_edge = Edge(orientation=Orientation.TOP, shape=Shape.OUTER, parent_piece=piece)
    right_edge = Edge(orientation=Orientation.RIGHT, shape=Shape.INNER, parent_piece=piece)
    bottom_edge = Edge(orientation=Orientation.BOTTOM, shape=Shape.INNER, parent_piece=piece)
    
    edges: Dict[Orientation, Edge] = {
        Orientation.LEFT: left_edge,
        Orientation.TOP: top_edge,
        Orientation.RIGHT: right_edge,
        Orientation.BOTTOM: bottom_edge,
        
    }
    piece.edges = edges
    
    piece.set_edge_as_orientation()
    
    