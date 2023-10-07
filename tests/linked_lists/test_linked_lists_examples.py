import pytest

from linked_lists.linked_lists_examples import LinkedList, Node

@pytest.fixture
def with_duplicates():
    node_e = Node(value=11, next=None)
    node_d = Node(value=12, next=node_e)
    node_c = Node(value=11, next=node_d)
    node_b = Node(value=13, next=node_c)
    node_a = Node(value=13, next=node_b)
    
    return LinkedList(head=node_a)


@pytest.fixture
def for_partition():
    node_g = Node(value=1, next=None)
    node_f = Node(value=2, next=node_g)
    node_e = Node(value=10, next=node_f)
    node_d = Node(value=5, next=node_e)
    node_c = Node(value=8, next=node_d)
    node_b = Node(value=5, next=node_c)
    node_a = Node(value=3, next=node_b)
    
    return LinkedList(head=node_a)
    

def test_remove_dups_when_removed_then_linked_list_has_no_dups(with_duplicates):
    with_duplicates.remove_dups()
    
    assert with_duplicates.head.value == 13
    assert with_duplicates.head.next.value == 11
    assert with_duplicates.head.next.next.value == 12
    assert with_duplicates.head.next.next.next is None
    

def test_remove_dups_in_place_when_removed_then_linked_list_has_no_dups(with_duplicates):
    with_duplicates.remove_dups_in_place()
    
    assert with_duplicates.head.value == 13
    assert with_duplicates.head.next.value == 11
    assert with_duplicates.head.next.next.value == 12
    assert with_duplicates.head.next.next.next is None
    
    
def test_kth_to_last_when_found_then_value_is_as_expected(with_duplicates):
    node = with_duplicates.kth_to_last(2)
    
    assert node.value == 12
    
    
def test_delete_node_when_deleted_then_remaining_linked_list_as_expected(with_duplicates):
    to_delete = with_duplicates.head.next.next  # 11
    
    with_duplicates.delete_node(to_delete)
    
    assert with_duplicates.head.value == 13
    assert with_duplicates.head.next.value == 13
    assert with_duplicates.head.next.next.value == 12
    assert with_duplicates.head.next.next.next.value == 11
    assert with_duplicates.head.next.next.next.next is None
    
    
def test_partition_when_paritioned_then_divided_as_expected(for_partition):
    for_partition.partition(5)
    # 3 5 8 5 10 2 1
    # 3 2 1 5 8 5 10
    
    assert for_partition.head.value == 3
    assert for_partition.head.next.value == 2
    assert for_partition.head.next.next.value == 1
    assert for_partition.head.next.next.next.value == 5
    assert for_partition.head.next.next.next.next.value == 8
    assert for_partition.head.next.next.next.next.next.value == 5
    assert for_partition.head.next.next.next.next.next.next.value == 10