import pytest

from linked_lists.linked_lists_examples import LinkedList, Node, intersection, sum_lists

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
    
    
@pytest.fixture
def sum_a():
    node_c = Node(value=6, next=None)
    node_b = Node(value=1, next=node_c)
    node_a = Node(value=7, next=node_b)
    
    return LinkedList(head=node_a)


@pytest.fixture
def sum_b():
    node_c = Node(value=2, next=None)
    node_b = Node(value=9, next=node_c)
    node_a = Node(value=5, next=node_b)
    
    return LinkedList(head=node_a)


@pytest.fixture
def palindrome():
    node_e = Node(value=1, next=None)
    node_d = Node(value=2, next=node_e)
    node_c = Node(value=3, next=node_d)
    node_b = Node(value=2, next=node_c)
    node_a = Node(value=1, next=node_b)
    
    return LinkedList(head=node_a)


@pytest.fixture
def not_palindrome():
    node_e = Node(value=1, next=None)
    node_d = Node(value=2, next=node_e)
    node_c = Node(value=3, next=node_d)
    node_b = Node(value=3, next=node_c)
    node_a = Node(value=1, next=node_b)
    
    return LinkedList(head=node_a)

@pytest.fixture
def with_loop():
    node_e = Node(value=5, next=None)
    node_d = Node(value=4, next=node_e)
    node_c = Node(value=3, next=node_d)
    node_b = Node(value=2, next=node_c)
    node_a = Node(value=1, next=node_b)
    node_e.next = node_c
    
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
    

def test_sum_lists_when_summed_then_sum_is_as_expected(sum_a, sum_b):
    sum = sum_lists(sum_a, sum_b)
    
    assert sum.head.value == 2
    assert sum.head.next.value == 1
    assert sum.head.next.next.value == 9
    

def test_is_palindrome_when_palindrome_then_returns_true(palindrome):
    result = palindrome.is_palindrome()
    assert result is True
    

def test_is_palindrome_when_not_palindrome_then_returns_false(not_palindrome):
    result = not_palindrome.is_palindrome()
    assert result is False
    
    
def test_reverse_when_reversed_then_in_correct_order(not_palindrome):
    reversed = not_palindrome.reverse()
    
    assert reversed.head.value == 1
    assert reversed.head.next.value == 2
    assert reversed.head.next.next.value == 3
    assert reversed.head.next.next.next.value == 3
    assert reversed.head.next.next.next.next.value == 1
    
    
def test_is_equal_when_equal_then_returns_true(palindrome):
    result = palindrome.is_equal(palindrome)
    
    assert result is True
    
    
def test_is_equal_when_not_equal_then_returns_false(palindrome, not_palindrome):
    result = palindrome.is_equal(not_palindrome)
    
    assert result is False
    
    
# 10 -> 1 -> 2 -> 3
# 20 -> 21 -> 1 -> 2 -> 3
def test_intersection_when_intersecting_then_returns_intersecting_node():
    inter_c = Node(value=3, next=None)
    inter_b = Node(value=2, next=inter_c)
    inter = Node(value=1, next=inter_b)
    
    a_head = Node(value=10, next=inter)
    
    b_head_next = Node(value=21, next=inter)
    b_head = Node(value=20, next=b_head_next)
    
    result = intersection(LinkedList(head=a_head), LinkedList(head=b_head))
    
    assert result == inter
    

def test_intersection_when_not_intersecting_then_returns_none(sum_a, sum_b):
    result = intersection(sum_a, sum_b)
    
    assert result is None
    
    
def test_get_last_node_details_when_obtained_then_as_expected(sum_a):
    details = sum_a.get_last_node_details()
    
    assert details.length == 3
    assert details.last.value == 6
    
    
def test_get_loop_when_loop_exists_then_return_first_node_of_loop(with_loop):
    loop = with_loop.get_loop()
    
    assert loop.value == 3
   
    
def test_has_loop_when_no_loop_exists_then_returns_none(with_duplicates):
    loop = with_duplicates.get_loop()
    
    assert loop is None
