from dataclasses import dataclass
from typing import Set


@dataclass
class Node:
    value: int
    next: 'Node' 


class LinkedList:
    head: Node
    
    def __init__(self, head: Node) -> None:
        self.head = head
    
    # 2.1 - Remove Dups: Write code to remove duplicates from an unsorted linked list.
    # How would you solve the problem if a temporary buffer in not allowed?
    def remove_dups(self) -> None:
        values: Set[int] = set()
        current = self.head
        
        while current and current.next:
            values.add(current.value)
            next_value = current.next.value
            
            if next_value in values:
                current.next = current.next.next
                
            current = current.next
        
    def remove_dups_in_place(self) -> None:
        current = self.head
        
        while current:
            runner = current
            while runner and runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                
                runner = runner.next
                
            current = current.next
        
    # 2.2 - Return Kth to Last: Implement and algorithm to find the kth to last element of a singly linked list.
    def kth_to_last(self, k: int) -> Node:
        right = self.head
        right_position = 1
        
        while right and right_position <= k:
            right = right.next
            right_position +=1
            
        left = self.head if right else None
            
        while right:
            left = left.next
            right = right.next
        
        return left
    
    # 2.3 - Delete Middle Node: Implement and algorithm to delete a node in the middle(i.e. any node but the first and last node, not necessarily the exact middle),
    # of a singly linked list, given only access to that node.
    def delete_node(self, node: Node) -> None:
        current = self.head
        
        while current and current.next:
            if current.next == node:
                current.next = current.next.next
                return
            
            current = current.next
            
    # 2.4 - Partition: Write code to partition a linked list around a value x, such that such that all nodes less than x come before all nodes greater than or equal to x.
    # 3 5 8 5 10 2 1
    # 3 2 1 5 8 5 10
    def partition(self, value: int) -> None:
        less_than = None
        greater_than_equal = None
        left_head = None
        right_head = None
        current = self.head
        
        while current:
            if current.value < value:
                if not left_head:
                    left_head = current
                if not less_than:
                    less_than = current
                else:
                    less_than.next = current
                    less_than = less_than.next
            else:
                if not right_head:
                    right_head = current
                if not greater_than_equal:
                    greater_than_equal = current
                else:
                    greater_than_equal.next = current
                    greater_than_equal = greater_than_equal.next
        
            current = current.next
                    
        if less_than:
            less_than.next = right_head
        
        self.head = left_head if left_head else right_head
        