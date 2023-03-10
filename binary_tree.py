from dataclasses import dataclass
from typing import Optional
from node import Node


@dataclass
class BinaryTree:
    root: Node
    
    def paths_from_root_summing_to(self, target: int) -> list[list[int]]:
        paths = _sums_from(self.root, [], target)
        
        return paths
    
    def lca(self, left: int, right: int) -> Optional[int]:
        lca: Node = None
        left_found = False
        right_found = False
        queue = [self.root]
        
        while queue and not (left_found and right_found):
            current_node = queue.pop(0)
            if current_node.left and current_node.left.value == left:
                left_found = True
                lca = current_node.value if lca is None else lca
            if current_node.right and current_node.right.value == right:
                right_found = True
                lca = current_node.value if lca is None else lca
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return lca if left_found and right_found else None


def _sums_from(node: Node, current_path: list[int], target: int) -> list[list[int]]:
    successful_paths = []
    updated_path = current_path.copy()
    
    if not node:
        return successful_paths
        
    updated_path.append(node.value)
    
    if sum(updated_path) == target:
        successful_paths.append(updated_path)
        
    left = _sums_from(node.left, updated_path, target)
    if left:
        successful_paths += left
    
    right = _sums_from(node.right, updated_path, target)
    if right:
        successful_paths += right
        
    return successful_paths
