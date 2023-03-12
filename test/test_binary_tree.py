import pytest

from binary_tree import BinaryTree
from node import Node


#          1
#   20            3
#            4        15
#          6   7    8    9
@pytest.fixture
def tree_a():
    node_9 = Node(value=9, left=None, right=None)
    node_8 = Node(value=8, left=None, right=None)
    node_15 = Node(value=15, left=None, right=None)
    node_7 = Node(value=7, left=None, right=None)
    node_6 = Node(value=6, left=None, right=None)
    node_4 = Node(value=4, left=None, right=None)
    node_3 = Node(value=3, left=None, right=None)
    node_20 = Node(value=20, left=None, right=None)
    root = Node(value=1, left=None, right=None)
    
    node_15.left = node_8
    node_15.right = node_9
    
    node_4.left = node_6
    node_4.right = node_7
    
    node_3.left = node_4
    node_3.right = node_15
    
    root.left = node_20
    root.right = node_3
    return BinaryTree(root=root)


#           10
#    28            13
#              14       15
#            21  22   23  24
@pytest.fixture
def tree_b():
    node_24 = Node(value=24, left=None, right=None)
    node_23 = Node(value=23, left=None, right=None)
    node_22 = Node(value=22, left=None, right=None)
    node_21 = Node(value=21, left=None, right=None)
    node_15 = Node(value=15, left=None, right=None)
    node_14 = Node(value=14, left=None, right=None)
    node_13 = Node(value=13, left=None, right=None)
    node_28 = Node(value=28, left=None, right=None)
    root = Node(value=10, left=None, right=None)
    
    node_15.left = node_23
    node_15.right = node_24
    
    node_14.left = node_21
    node_14.right = node_22
    
    node_13.left = node_14
    node_13.right = node_15
    
    root.left = node_28
    root.right = node_13
    return BinaryTree(root=root)


#              4
#       2            5
#    1    3       
@pytest.fixture
def binary_search_tree_a():
    node_3 = Node(value=3, left=None, right=None)
    node_1 = Node(value=1, left=None, right=None)
    node_5 = Node(value=5, left=None, right=None)
    node_2 = Node(value=2, left=node_1, right=node_3)
    root = Node(value=4, left=node_2, right=node_5)
    
    return BinaryTree(root=root)
    

def test_paths_from_root_summing_to_when_single_path_exists_then_returns_path(tree_a):
    expected_path = [1, 3, 4]
    
    paths = tree_a.paths_from_root_summing_to(8)
    
    assert len(paths) == 1
    only_path = paths[0]
    assert only_path == expected_path
    

def test_paths_from_root_summing_to_when_multiple_paths_exist_then_returns_paths(tree_b):
    expected_first_path = [10, 28]
    expected_second_path = [10, 13, 15]
    
    paths = tree_b.paths_from_root_summing_to(38)
    
    assert len(paths) == 2
    assert paths[0] == expected_first_path
    assert paths[1] == expected_second_path
    

@pytest.mark.parametrize(
    "left,right,expected",
    [
        pytest.param(20, 9, 1),
        pytest.param(6, 7, 4),
        pytest.param(6, 101, None),
        pytest.param(101, 7, None),
    ]
)
def test_lca_when_both_nodes_exist_then_returns_lca(left, right, expected, tree_a):
    actual = tree_a.lca(left, right)
    
    assert actual == expected
    
    
def test_is_bst_when_bst_then_returns_true(binary_search_tree_a):
    assert binary_search_tree_a.is_bst() is True
    

def test_is_bst_when_not_bst_then_returns_false(tree_a, tree_b):
    assert tree_a.is_bst() is False
    assert tree_b.is_bst() is False