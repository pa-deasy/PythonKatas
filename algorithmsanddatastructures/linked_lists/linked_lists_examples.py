from dataclasses import dataclass
from typing import Any, List, Set, Tuple


@dataclass
class Node:
    value: Any
    next: 'Node' 
    
    
@dataclass
class LastNodeDetails:
    length: int
    last: Node


class LinkedList:
    head: Node
    
    def __init__(self, head: Node = None) -> None:
        self.head = head
        
    # 2.1 - Remove Dups: Write code to remove duplicates from an unsorted linked list.
    # How would you solve the problem if a temporary buffer in not allowed?
    def remove_duplicates(self) -> None:
        current = self.head
        if current is None:
            return 
        
        values = set()
        while current.next:
            values.add(current.value)
            if current.next.value in values:
                current.next = current.next.next
            else:
                current = current.next
        
    def remove_duplicates_in_place(self) -> None:
        current = self.head
        while current:
            runner = current
            while runner and runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            current = current.nextd
        
    # 2.2 - Return Kth to Last: Implement and algorithm to find the kth to last element of a singly linked list.
    def kth_to_last(self, k: int) -> Node:
        right = self.head
        
        right_position = 0

        while right and right_position < k:
            right = right.next
            right_position += 1
        
        left = self.head if right_position == k else None

        while right:
            right = right.next
            left = left.next

        return left
    
    # 2.3 - Delete Middle Node: Implement and algorithm to delete a node in the middle(i.e. any node but the first and last node, not necessarily the exact middle),
    # of a singly linked list, given only access to that node.
    def delete_node(self, node: Node) -> None:
        if not node or not node.next:
            node = None    
        else:
            node.value = node.next.value
            node.next = node.next.next
            
    # 2.4 - Partition: Write code to partition a linked list around a value x, such that such that all nodes less than x come before all nodes greater than or equal to x.
    # 3 5 8 5 10 2 1
    # 3 2 1 5 8 5 10
    def partition(self, value: int) -> None:
        left = None
        right = None
        right_head = None
        node = self.head

        while node:
            if node.value < value:
                if left:
                    left.next = node
                left = node
            else:
                if right:
                    right.next = node
                else:
                    right_head = node
                right = node
            node = node.next
        
        if left:
            left.next = right_head
            self.head = left
        else:
            self.head = right
        
    # 2.6 - Palindrome: Implement a function to check if a linked list is a palindrome
    def is_palindrome(self):
        reversed = self.reverse()
        
        return self.is_equal(reversed)
    
    def reverse(self) -> 'LinkedList':
        new_head = None
        current = self.head
        
        while current:
            node = Node(value=current.value, next=new_head)
            new_head = node
            current = current.next
            
        return LinkedList(head=new_head)
    
    def is_equal(self, other: 'LinkedList') -> bool:
        current_self = self.head
        current_other = other.head
        
        while current_self and current_other:
            if current_self.value != current_other.value:
                return False
            
            current_self = current_self.next
            current_other = current_other.next
            
        return False if current_self or current_other else True
    
    def get_last_node_details(self) -> LastNodeDetails:
        if not self.head:
            return LastNodeDetails(length=0, last=None)
        
        length = 1
        current = self.head
        while current and current.next:
            length += 1
            current = current.next
        
        return LastNodeDetails(length=length, last=current)
    
    
    # 2.8 - Loop Detection: Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop(if one exists).
    def get_loop(self) -> Node:
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
            
        slow = self.head
        
        while fast.next:
            if slow == fast:
                return slow
            
            slow = slow.next
            fast = fast.next
        
        return None
    
    def remove_first(self) -> Node:
        if not self.head:
            return None
        
        node = self.head
        self.head = self.head.next
        return node
        
    def remove_last(self) -> Node:
        if not self.head or not self.head.next:
            self.head = None
            
        current = self.head
        while current and current.next.next:
            current = current.next
        
        node = current.next
        current.next = None
        return node
        
    def insert_first(self, node: Node) -> None:
        node.next = self.head
        self.head = node
        
    def insert_last(self, node: Node) -> None:
        if not self.head:
            self.head = node
        
        current = self.head
        while current and current.next:
            current = current.next
            
        current.next = node
    
    def to_list(self) -> List[int]:
        numbers = []
        if not self.head:
            return numbers
        
        current = self.head
        while current:
            numbers.append(current.value)
            current = current.next
            
        return numbers
    
    def clone(self) -> 'LinkedList':
        cloned_head=Node(value=self.head.value, next=None)
        
        cloned = cloned_head
        current = self.head.next
        while current:
            node = Node(value=current.value, next=None)
            cloned.next = node
            cloned = node
            current = current.next
            
        return LinkedList(head=cloned_head)
    
    def add_all(self, other: 'LinkedList') -> None:
        cloned = other.clone()
        self.insert_last(cloned.head)

    def length(self) -> int:
        node = self.head
        count = 0

        while node:
            count += 1
            node = node.next

        return count
    
    def pad(self, count: int) -> None:
        while count > 0:
            node = Node(value=0, next=self.head)
            self.head = node
            count -= 1
    
        

# 2.5 - Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum of the linked list.
# (You are not allowed to cheat and just convert the list to an integer.)
# Input (7 -> 1 -> 6) + (5 -> 9 -> 2) That is, 617 + 295
# Output 2 -> 1 -> 9 that is, 912
def sum_lists(a: LinkedList, b :LinkedList) -> LinkedList:
    sum = _sum(a.head, b.head, 0)
    return LinkedList(head=sum)

def _sum(a: Node, b :Node, carryover: int) -> LinkedList:
    if not a and not b and carryover == 0:
        return None
    
    value = carryover
    if a:
        value += a.value
    if b:
        value += b.value
    
    result = Node(value=value % 10, next=None)
    
    if a or b:
        next = _sum(a.next if a else None, b.next if b else None, 1 if value >= 10 else 0)
        result.next = next
    
    return result
    

def reverse_sum(a: LinkedList, b: LinkedList) -> LinkedList:
    a_length = a.length()
    b_length = b.length()
    shorter, longer = (a, b) if a_length < b_length else (b, a)
    shorter.pad(abs(a_length - b_length))

    node, remainder = _reverse_sum(shorter.head, longer.head)
    if remainder > 0:
        node = Node(value=remainder, next=node)

    return LinkedList(head=node)

def _reverse_sum(a: Node, b: Node) -> Tuple[Node, int]:
    if a.next is None and b.next is None:
        sum, remainder = _get_sum_and_remainder(a.value + b.value)
        return Node(value=sum, next=None), remainder
    
    next_node, next_remainder = _reverse_sum(a.next, b.next)
    sum, remainder = _get_sum_and_remainder(a.value + b.value + next_remainder)
    return Node(value=sum, next=next_node), remainder

def _get_sum_and_remainder(sum: int) -> Tuple[int, int]:
    remainder = 0
    if sum >= 10:
        sum = sum % 10
        remainder = 1

    return sum, remainder
    
# 2.7 - Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is definded based on reference, not value. That is, if the kth node of the first linked list is the exact same node(by reference) as the jth node of the second list, then they are intersecting.
def intersection(a: LinkedList, b: LinkedList) -> Node:    
    a_last_node_details = a.get_last_node_details()
    b_last_node_details = b.get_last_node_details()
    
    if a_last_node_details.last != b_last_node_details.last:
        return None
    
    longer, shorter = (a.head, b.head) if a_last_node_details.length > b_last_node_details.length else (b.head, a.head)
    
    diff = abs(a_last_node_details.length - b_last_node_details.length)
    
    diff_counter = 0
    while diff_counter < diff:
        longer = longer.next
        diff_counter += 1
        
    while longer and shorter:
        if longer == shorter:
            return longer
        
        longer = longer.next
        shorter = shorter.next
        
    return None

