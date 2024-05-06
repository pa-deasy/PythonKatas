from dataclasses import dataclass
import math
from queue import Queue
import random
from typing import Dict, List, Set, Tuple

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

            
# 4.4 - Check Balanced: Implement a function to check if a binary tree is balanced. 
# For the purpose of this question, a balanced tree is defined to be a tree such that the height of the two subtrees of any node never differ by more than one.
@dataclass
class TreeDetails:
    min_height: int = None
    max_height: int = None


def check_is_balanced_tree(node: TreeNode) -> bool:
    details = get_tree_details(node, 0, TreeDetails())
    return details.max_height - details.min_height <= 1


def get_tree_details(node: TreeNode, count: int, details: TreeDetails) -> TreeDetails:
    if not node:
        details.min_height = count if not details.min_height or details.min_height > count else details.min_height
        details.max_height = count if not details.max_height or details.max_height < count else details.max_height
        return details
    
    get_tree_details(node.left, count + 1, details)
    get_tree_details(node.right, count + 1, details)
    
    return details


# 4.5 - Validate BST - Implement a function to check if a binary tree is a binary search tree.
def check_is_bst(node: TreeNode, min: int = None, max: int = None) -> bool:
    if node is None:
        return True
    
    if min and node.value <= min or max and node.value > max:
        return False
    
    left = check_is_bst(node.left, min, node.value)
    right = check_is_bst(node.right, node.value, max)
    
    return left and right


# 4.6 - Successor: Write an algorithm to find the "next" node(i.e. in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to it's parent.
def get_in_order_successor(node: TreeNode) -> TreeNode:
    if not node:
        return None
    
    if node.right:
        return _left_most_child(node.right)
    else:
        other = node
        other_parent = other.parent
        while other_parent and other_parent.left != other:
            other = other_parent
            other_parent = other_parent.parent
        return other_parent
    
    
def _left_most_child(node: TreeNode) -> TreeNode:
    if not node:
        return None
    
    while node.left:
        node = node.left
        
    return node


# 4.7 Build Order: You are given a list of projects and a list of dependencies(which is a list of pairs of projects, where the second project is dependent on the first project).
# All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built.
# If no valid build order, return error.
# Input -  projects: a, b, c, d, e, f       dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output - f, e, a, b, d, c 
# a: f
# b: f
# c: d
# d: a b
# e
# f: 
def get_build_order(projects: list[str], dependencies: list[Tuple[str, str]]) -> list[str]:
    empty_map: Dict[str, list[str]] = _generate_dependencies_map(projects)
    (map, roots) = _populate_dependencies_map_and_roots(empty_map, dependencies)
    
    roots.sort(reverse=True)
    order: list[str] = []
    visited: Set[int] = set()
    while roots:
        value = roots.pop(0)
        
        if value in visited:
            continue
        
        order.insert(0, value)
        visited.add(value)
        roots += map[value]
            
    return order

    
def _generate_dependencies_map(projects: list[str]) -> Dict[str, list[str]]:
    map: Dict[str, list[str]] = {}
    
    for p in projects:
        map[p] = []
        
    return map    
    
    
def _populate_dependencies_map_and_roots(map: Dict[str, list[str]], dependencies: list[Tuple[str, str]]) -> Tuple[Dict[str, list[str]], list[str]]:
    potential_roots = set(map.keys())
    for (d_to, d_from) in dependencies:
        dependents = map[d_from]
        dependents.append(d_to)
        map[d_from] = dependents
        potential_roots.discard(d_to)
        
    return (map, list(potential_roots))


# 4.8 - First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
# This is not necessarily a binary search tree.
def get_first_common_ancestor(root: TreeNode, left: int, right: int) -> TreeNode:
    if not root:
        return None
    
    left_contains = check_contains(root.left, left)
    right_contains = check_contains(root.right, right)
    
    if left_contains and right_contains:
        return root
    elif left_contains:
        return get_first_common_ancestor(root.left, left, right)
    elif right_contains:
        return get_first_common_ancestor(root.right, left, right)
    else:
        return None


def check_contains(root: TreeNode, value: int) -> bool:
    if not root:
        return False
    
    if root.value == value:
        return True
    
    left = check_contains(root.left, value)
    right = check_contains(root.right, value)
    
    return left or right


def return_contains(root: TreeNode, value: int) -> TreeNode:
    if not root:
        return None
    
    if root.value == value:
        return root
    
    left = return_contains(root.left, value)
    right = return_contains(root.right, value)
    
    return left if left else right


# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
def get_all_sequences(node: TreeNode) -> List[List[int]]:
    result: List[LinkedList] = []
    
    if not node:
        result.append(LinkedList(head=None))
        return result
    
    prefix = LinkedList(head=Node(value=node.value, next=None))
    
    left_seq = get_all_sequences(node.left)
    right_seq = get_all_sequences(node.right)
    
    for left in left_seq:
        for right in right_seq:
            weaved: List[LinkedList] = []
            _weave_lists(left, right, weaved, prefix)
            result += weaved
            
    return result


def _weave_lists(first: LinkedList, second: LinkedList, results: List[LinkedList], prefix: LinkedList) -> None:
    if not first or not second:
        result = prefix.clone()
        result.add_all(first)
        result.add_all(second)
        results.append(result)
        return
    
    head_first = first.remove_first()
    prefix.insert_last(head_first)
    _weave_lists(first, second, results, prefix)
    prefix.remove_last()
    first.insert_first(head_first)
    
    head_second = second.remove_first()
    prefix.insert_last(head_second)
    _weave_lists(first, second, results, prefix)
    prefix.remove_last()
    second.insert_first(head_second)


# 4.10 - Check Subtree: T1 an T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there existsa node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the tree would be identical.
def check_is_subtree(node: TreeNode, subtree: TreeNode) -> bool:
    match = return_contains(node, subtree.value)
    
    if not match:
        return False
    
    is_equal = check_is_equal(match, subtree)
    
    return is_equal
    
    
def check_is_equal(a: TreeNode, b: TreeNode) -> bool:
    if not a and not b:
        return True
    
    if not a or not b:
        return False
    
    equal = a.value == b.value
    left_equal = check_is_equal(a.left, b.left)
    right_equal = check_is_equal(a.right, b.right)
    
    return equal and left_equal and right_equal


def get_node_count(node: TreeNode) -> int:
    if not node:
        return 0
    
    total = 1
    total += get_node_count(node.left)
    total += get_node_count(node.right)
    
    return total


# 4.11 - Random Node: You are implementing a binary search tree class from scratch which, in addition to insert, find and delete, has a method getRandomNode() which returns a random node from the tree.
# All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.
def to_list(node: TreeNode, numbers: List[int] = []) -> List[int]:
    if node is None:
        return numbers
    
    numbers.append(node.value)
    
    to_list(node.left)
    to_list(node.right)
    
    return numbers


def get_random_node(node: TreeNode) -> Node:
    numbers = to_list(node)
    guess = random.choice(numbers)
    
    return guess


# 4.12 - Paths with Sums: You are given a binary tree in which each node contains an integer value(which might be positive or negative).
# Design an algorithm to count the number of paths that sum to a given value. 
# The path does not need to start or end at the root or a leaf but it must go downwards(traveling only from parent nodes to childs nodes).
def get_count_of_sums(node: TreeNode, target: int, current: int = 0, current_count = 0) -> int:
    count = 0
    if not node:
        return count
    
    current += node.value
    
    if current == target:
        count += current_count + 1
        
    left = get_count_of_sums(node.left, target, current, count)
    left_from_zero = get_count_of_sums(node.left, target, 0, count)
    right = get_count_of_sums(node.right, target, current, count)
    right_from_zero = get_count_of_sums(node.right, target, 0, count)
    
    # return left + left_from_zero + right + right_from_zero
    return count + left + right + left_from_zero + right_from_zero