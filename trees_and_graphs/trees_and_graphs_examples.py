from dataclasses import dataclass


# 4.1 - Route Between Nodes: Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.
@dataclass
class Node:
    name: str
    children: list['Node']
    visited: bool = False


def check_route_exists(start: Node, end: Node) -> bool:
    return _check_target_exists(start, end.name)


def _check_target_exists(current: Node, target: str) -> bool:
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


