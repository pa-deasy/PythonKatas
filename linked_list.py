from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: 'Node'


@dataclass
class LinkedList:
    head: Node
    
    def node_at_position(self, position):
        current_node = self.head
        counter = 0
        
        while counter < position:
            if not current_node.next:
                return None
            
            current_node = current_node.next
            counter +=1
        
        return current_node
    
    def push(self, new_node: Node) -> None:
        new_node.next = self.head
        self.head = new_node
    
    def length(self):
        if not self.head:
            return 0
        
        current_node = self.head
        counter = 1
        
        while current_node.next:
            current_node = current_node.next
            counter +=1
        
        return counter
        
    def last_to_front(self) -> None:
        length = self.length()
        last_node = self.node_at_position(length - 1)
        second_last_node = self.node_at_position(length - 2)
        
        second_last_node.next = None
        self.push(last_node)
        
    def reverse(self) -> None:
        current_node = self.head
        
        while current_node and current_node.next:
            next = current_node.next
            current_node.next = next.next
            self.push(next)
            
    def another_reverse(self) -> None:
        for index in range(1, self.length()):
            current_node = self.node_at_position(index)
            previous_node = self.node_at_position(index - 1)
            previous_node.next = current_node.next
            self.push(current_node)

    def pair_wise_swap(self) -> None:
        current_node = self.head
        if current_node.next:
            self.head = current_node.next
        
        while current_node and current_node.next:
            next = current_node.next
            current_node.next = next.next
            next.next = current_node
            current_node = current_node.next