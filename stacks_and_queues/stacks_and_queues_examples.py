# 3.1 - Three in one: Describe how you could use a single array to implement three stacks.
import math


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
            return
        
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