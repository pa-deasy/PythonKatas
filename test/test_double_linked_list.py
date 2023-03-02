import pytest

from double_linked_list import Node, DoubleLinkedList


@pytest.fixture
def some_double_linked_list():
    third_node = Node(value=30, previous=None, next=None)
    second_node = Node(value=20, previous=None, next=third_node)
    head = Node(value=10, previous=None, next=second_node)
    third_node.previous = second_node
    second_node.previous = head
    return DoubleLinkedList(head=head)


def test_node_at_position_when_node_exists_then_is_returned(some_double_linked_list):
    first = some_double_linked_list.node_at_position(0)
    second = some_double_linked_list.node_at_position(1)
    third = some_double_linked_list.node_at_position(2)
    
    assert first.value == 10
    assert second.value == 20
    assert third.value == 30
    

def test_push_when_node_pushed_then_head_as_expected(some_double_linked_list):
    new_node = Node(value=90, previous=None, next=None)
    some_double_linked_list.push(new_node)
    
    assert some_double_linked_list.node_at_position(0).value == 90
    assert some_double_linked_list.node_at_position(1).value == 10
    assert some_double_linked_list.node_at_position(2).value == 20
    assert some_double_linked_list.node_at_position(3).value == 30
    
    
def test_reverse_when_reversed_then_nodes_ordered_as_expected(some_double_linked_list):
    some_double_linked_list.reverse()
    
    first = some_double_linked_list.node_at_position(0)
    second = some_double_linked_list.node_at_position(1)
    third = some_double_linked_list.node_at_position(2)
    
    assert first.value == 30
    assert first.next.value == 20
    assert first.previous == None
    
    assert second.value == 20
    assert second.next.value == 10
    assert second.previous.value == 30
    
    assert third.value == 10
    assert third.next == None
    assert third.previous.value == 20
