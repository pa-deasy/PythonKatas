from dataclasses import dataclass
from node import Node


@dataclass
class BinaryTree:
    root: Node
    
    def paths_from_root_summing_to(self, target: int) -> list[list[int]]:
        paths = sums_from(self.root, [], target)
        
        return paths



def sums_from(node: Node, current_path: list[int], target: int) -> list[list[int]]:
    successful_paths = []
    updated_path = current_path.copy()
    
    if not node:
        return successful_paths
        
    updated_path.append(node.value)
    
    if sum(updated_path) == target:
        successful_paths.append(updated_path)
        
    left = sums_from(node.left, updated_path, target)
    if left:
        successful_paths += left
    
    right = sums_from(node.right, updated_path, target)
    if right:
        successful_paths += right
        
    return successful_paths
    