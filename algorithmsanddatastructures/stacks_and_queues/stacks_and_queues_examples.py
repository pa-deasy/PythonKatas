from dataclasses import dataclass
from enum import Enum
import math
from typing import List


# 3.1 - Three in one: Describe how you could use a single array to implement three stacks.
class MultiStack:
    stack_count: int
    stack_size: int
    values: list[int]
    sizes: list[int]
    
    def __init__(self, stack_count: int, total_size: int) -> None:
        self.stack_count = stack_count
        self.stack_size = math.floor(total_size / stack_count)
        self.values = [None for r in range(total_size)]
        self.sizes = [0 for r in range(stack_count)]
    
    def push(self, stack_number: int, value: int) -> None:
        if self.is_full(stack_number):
            print(f'Stack {stack_number} is full')
            return
        
        self.sizes[stack_number - 1] += 1
        top = self.top_index(stack_number)
        self.values[top] = value
        
    def peek(self, stack_number: int) -> int:
        top = self.top_index(stack_number)
        return self.values[top]
        
    def pop(self, stack_number: int) -> int:
        if self.is_empty(stack_number):
            print(f'Stack {stack_number} is empty')
            return None
        
        top = self.top_index(stack_number)
        popped = self.values[top]
        self.values[top] = None
        self.sizes[stack_number - 1] -= 1
        
        return popped
    
    def is_empty(self, stack_number: int) -> bool:
        return self.sizes[stack_number - 1] == 0
        
    def is_full(self, stack_number: int) -> bool:
        return self.sizes[stack_number - 1] == self.stack_size
    
    def top_index(self, stack_number: int) -> int:
        offset = (stack_number - 1) * self.stack_size
        
        return offset + self.sizes[stack_number - 1] - 1
    

# 3.2 - Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
# Push, pop and min should all operate in O(1) time.
class Stack:
    values: list[int]
    
    def __init__(self) -> None:
        self.values = []
    
    def push(self, value: int) -> None:
        self.values.append(value)
        
    def peek(self) -> int:
        return self.values[-1] if self.values else None
        
    def pop(self) -> int:
        return self.values.pop()
    
    def size(self) -> int:
        return len(self.values)
    
    def is_empty(self) -> bool:
        return len(self.values) == 0
    
    
class MinStack(Stack):
    mins: Stack
    
    def __init__(self) -> None:
        self.mins = Stack()
        super().__init__()
        
    def push(self, value: int) -> None:
        super().push(value)
        if not self.mins.peek() or value < self.mins.peek():
            self.mins.push(value)
            
    def pop(self) -> int:
        popped = super().pop()
        if self.mins.peek() and self.mins.peek() == popped:
            self.mins.pop()
        return popped
        
    def min(self) -> int:
        return self.mins.peek()
    
    
# 3.3 - Stack of Plates: Imagine a stack of plates. If the stack gets too high, it might topple. 
# Therefore in real life, we would likey start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. It should be composed of several stacks and should create a new stack once the previous one exceed capacity.
# Push and Pop should behave identically to the single stack. 
# Implement a function PopAt(index) which performs a pop operation on anu specific sub-stack.
class SetOfStacks:
    stack_size: int
    stacks: List[Stack]
    stack_index: int
    
    def __init__(self, stack_size: int) -> None:
        self.stack_size = stack_size
        self.stacks = [Stack()]
        self.stack_index = 0
        
    def push(self, value: int) -> None:
        if (self.is_full(self.stack_index)):
            self._add_stack()
            
        self.stacks[self.stack_index].push(value)
        
    def peek(self) -> int:
        return self.stacks[self.stack_index].peek()
    
    def pop(self) -> int:
        popped = self.stacks[self.stack_index].pop()
        if self.stacks[self.stack_index].size() == 0:
            self._remove_stack()
            
        return popped
    
    def pop_at(self, index: int) -> int:
        if index > self.stack_index:
            return None
        
        return self.stacks[index].pop()
        
    
    def is_full(self, index: int) -> bool:
        if index > self.stack_index or self.stacks[index].size() < self.stack_size:
            return False
        
        return True
    
    def _add_stack(self) -> None:
        self.stacks.append(Stack())
        self.stack_index += 1
        
    def _remove_stack(self) -> None:
        self.stack_index -= 1
        self.stacks = self.stacks[:self.stack_index + 1]
        

# 3.4 - Queue via Stack: Implement a MyQueue class which implements a queue using two stacks.
class MyQueue:
    queue: Stack
    
    def __init__(self) -> None:
        self.queue = Stack()
    
    def enqueue(self, value: int) -> None:
        temporary = Stack()
        
        while not self.queue.is_empty():
            popped = self.queue.pop()
            temporary.push(popped)
        
        temporary.push(value)
        
        while not temporary.is_empty():
            popped = temporary.pop()
            self.queue.push(popped)
            
    def dequeue(self) -> int:
        return self.queue.pop()
    
    def peek(self) -> int:
        return self.queue.peek()
    
    
# 3.5 - Sort Stack: Write a program to sort a stack such that the smallest items are on the top. 
# You can use an additional temporary stack, but you may not copy the elements into any other data structure(such as an array).
def sort_stack(stack: Stack) -> Stack:
    other = Stack()
    
    while not stack.is_empty():
        temp = stack.pop()
        while not other.is_empty() and other.peek() > temp:
            stack.push(other.pop())
            
        other.push(temp)
        
    while not other.is_empty():
        stack.push(other.pop())
    
    return stack


# 3.6 - An animal shelter, which holds only dogs and cats, operateds on strictly "first in, first out" basis.
# People must adopt either the oldest(based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat(receive oldest of that type).
# They cannot select which specific animal they would like. Create the data structure to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
# You may use the build-in LinkedList datastructure.
class AnimalType(Enum):
    Dog = 'dog'
    Cat = 'cat'


@dataclass
class Animal:
    name: str
    type: AnimalType
    

@dataclass
class AnimalNode:
    value: Animal
    next: 'AnimalNode' 
    

class LinkedList:
    head: AnimalNode
    
    def __init__(self, head: AnimalNode) -> None:
        self.head = head
    
    def last(self) -> AnimalNode:
        if not self.head:
            return self.head
        
        current = self.head
        while current.next:
            current = current.next
            
        return current
    
    def first_of(self, type: AnimalType) -> AnimalNode:
        current = self.head
        
        while current:
            if current.value.type == type:
                return current
            
            current = current.next
            
        return None
    
    def remove_at(self, node: AnimalNode) -> None:
        if not node:
            return
        
        node.value = node.next.value
        node.next = node.next.next


class AnimalShelter:
    animals: LinkedList
    
    def __init__(self) -> None:
        self.animals = LinkedList(head=None)
        
    def enqueue(self, animal: Animal) -> None:
        node = AnimalNode(value=animal, next=None)
        last = self.animals.last()
        
        if not last:
            self.animals.head = node
        else:
            last.next = node
        
    def dequeue_any(self) -> Animal:
        oldest = self.animals.head
        self.animals.head = oldest.next
        
        return oldest.value if oldest else None
    
    def dequeue_dog(self) -> Animal:
        return self._dequeue_type(AnimalType.Dog)

    def dequeue_cat(self) -> Animal:
        return self._dequeue_type(AnimalType.Cat)
    
    def _dequeue_type(self, type: AnimalType) -> Animal:
        oldest = self.animals.first_of(type)
        dequeued = oldest.value if oldest else None
        
        self.animals.remove_at(oldest)
        
        return dequeued
    
    
    
    
        
    
        
        

# d d c d c c