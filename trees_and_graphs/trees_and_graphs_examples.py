from dataclasses import dataclass
import math
from queue import Queue
from typing import List

from linked_lists.linked_lists_examples import LinkedList, Node


# 4.1 - Route Between Nodes: Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.
@dataclass
class GraphNode:
    name: str
    children: list['GraphNode']
    visited: bool = False


def check_route_exists(start: GraphNode, end: GraphNode) -> bool:
    return _check_target_exists(start, end.name)


def _check_target_exists(current: GraphNode, target: str) -> bool:
    if not current or current.visited:
        return False
    
    current.visited = True
    
    if current.name == target:
        return True
    
    exists = False
    for child in current.children:
        child_exists = _check_target_exists(child, target)
        exists = exists or child_exists
        
    return exists


# 4.2 - Minimal Tree: Given a sorted(increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
@dataclass
class TreeNode:
    value: int
    left: 'TreeNode'
    right: 'TreeNode'
    

def create_bst_from_sorted_list(numbers: list[int]) -> TreeNode:
    if not numbers:
        return None
    
    mid = math.floor(len(numbers) / 2)
    left = create_bst_from_sorted_list(numbers[:mid])
    right = create_bst_from_sorted_list(numbers[mid+1:])
    node = TreeNode(value=numbers[mid], left=left, right=right)
    
    return node


# 4.3 - List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
# (e.g. if you have a tree with depth D, you'll have D linked lists).
def create_linked_lists_from_tree(root: TreeNode) -> List[LinkedList]:
    linked_lists: List[LinkedList] = []
    queue = [root]
    
    while queue:
        next_queue = []
        linked_list = LinkedList(head=None)
        
        while queue:
            dequeued = queue.pop(0)
            node = Node(value=dequeued.value, next=None)
            node.next = linked_list.head
            linked_list.head = node
            
            if dequeued.left:
                next_queue.append(dequeued.left)
            if dequeued.right:
                next_queue.append(dequeued.right)
        
        linked_lists.append(linked_list)    
        queue = next_queue
        
    return linked_lists
            
