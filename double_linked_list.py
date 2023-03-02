from dataclasses import dataclass


@dataclass
class Node:
    value: int
    previous: 'Node'
    next: 'Node'
    

@dataclass
class DoubleLinkedList:
    head: Node

    def node_at_position(self, position: int) -> Node:
        current_node = self.head
        counter = 0
        
        while counter < position:
            if not current_node.next:
                return None
            current_node = current_node.next
            counter += 1
            
        return current_node
    
    def push(self, new_node: Node) -> None:
        self.head.previous = new_node
        new_node.previous = None
        new_node.next = self.head
        self.head = new_node
    
    def reverse(self) -> None:
        current_node = self.head
        
        while current_node and current_node.next:
            next = current_node.next
            current_node.next = next.next
            self.push(next)
            