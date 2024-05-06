import base64
from dataclasses import dataclass
import hashlib
import math
from typing import Any, List, Optional


@dataclass
class LinkedListNode:
    key: Any
    value: Any
    next: 'LinkedListNode' = None
    previous: 'LinkedListNode' = None
    
    
class Hasher:
    array: List[LinkedListNode]
    
    def __init__(self, capacity: int) -> None:
        self.array = []
        for index in range(capacity):
            self.array.append(None)
            
    def put(self, key: Any, value: Any) -> Optional[Any]:
        node = self.get_node_for_key(key)
        if node:
            old_value = node.value
            node.value = value
            return old_value
        
        node = LinkedListNode(key=key, value=value)
        index = self.get_index_for_key(key)
        if self.array[index]:
            node.next = self.array[index]
            node.next.previous = node
        self.array[index] = node
        return None
    
    def remove(self, key: Any) -> Any:
        node = self.get_node_for_key(key)
        if not node:
            return None
        
        if node.previous:
            node.previous.next = node.next
        else:
            hash_key = self.get_index_for_key(key)
            self.array.insert(hash_key, node.next)
        
        if node.next:
            node.next.previous = node.previous
            
        return node.value
    
    def get(self, key: Any) -> Any:
        if not key:
            return None
        
        node = self.get_node_for_key(key)
        
        return node.value if node else None
    
    def get_index_for_key(self, key: Any) -> int:
        return abs(len(key) % len(self.array))
    
    def get_node_for_key(self, key: Any) -> LinkedListNode:
        index = self.get_index_for_key(key)
        current = self.array[index]
        while current:
            if current.key == key:
                return current
            current = current.next
            
        return None