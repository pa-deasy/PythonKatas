import pytest

from linked_list import LinkedList, Node


@pytest.fixture
def some_linked_list():
    third_node = Node(value=30, next=None)
    second_node = Node(value=20, next=third_node)
    head = Node(value=10, next=second_node)
    return LinkedList(head=head)
    

def test_node_at_position_when_node_exists_returns_node(some_linked_list):
    node_0 = some_linked_list.node_at_position(0)
    assert node_0.value == 10
    node_1 = some_linked_list.node_at_position(1)
    assert node_1.value == 20
    node_2 = some_linked_list.node_at_position(2)
    assert node_2.value == 30
  
    
def test_node_at_position_when_no_node_exists_returns_none(some_linked_list):
    node_4 = some_linked_list.node_at_position(4)
    assert node_4 == None
    

def test_push_when_pushed_then_new_node_at_front(some_linked_list):
    new_node = Node(value=9, next=None)
    
    some_linked_list.push(new_node)
    
    assert some_linked_list.node_at_position(0).value == 9
    assert some_linked_list.node_at_position(1).value == 10
    assert some_linked_list.node_at_position(2).value == 20
    assert some_linked_list.node_at_position(3).value == 30


def test_length_when_nodes_then_returns_length(some_linked_list):
    assert some_linked_list.length() == 3
    
    
def test_length_when_no_nodes_then_returns_zero(some_linked_list):
    no_head_linked_list = LinkedList(head=None)
    assert no_head_linked_list.length() == 0


def test_last_to_front_when_moved_then_new_node_at_front(some_linked_list):
    some_linked_list.last_to_front()
    
    assert some_linked_list.node_at_position(0).value == 30
    assert some_linked_list.node_at_position(1).value == 10
    assert some_linked_list.node_at_position(2).value == 20


def test_reverse_when_reversed_then_nodes_ordered_as_expected(some_linked_list):
    some_linked_list.reverse()

    assert some_linked_list.node_at_position(0).value == 30
    assert some_linked_list.node_at_position(1).value == 20
    assert some_linked_list.node_at_position(2).value == 10
    

def test_pair_wise_swap_when_swapped_then_nodes_ordered_as_expected(some_linked_list):
    some_linked_list.pair_wise_swap()
    
    assert some_linked_list.node_at_position(0).value == 20
    assert some_linked_list.node_at_position(1).value == 10
    assert some_linked_list.node_at_position(2).value == 30
