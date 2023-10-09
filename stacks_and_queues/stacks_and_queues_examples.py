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
        
        