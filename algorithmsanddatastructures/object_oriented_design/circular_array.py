# 7.9 - Circular Array: Implement a CircularArray class that supports an array-like data structure which can be efficiently rotated.
# If possible the class should use a generic type, and should support iteration via the standard for (obj o: circularArray) notation.
from typing import Any, List


class CircularArray:
    items: List[Any]
    head: int
    
    def __init__(self, items: List[Any]) -> None:
        self.items = items
        self.head = 0
        
    def convert(self, index: int) -> int:
        if index < 0:
            index += len(self.items)
        return (self.head + index) % len(self.items)
        
    def rotate(self, shift: int) -> None:
        self.head = self.convert(shift)
        
    def get(self, index: int) -> Any:
        if index < 0 or index >= len(self.items):
            raise Exception('Index out of range')
        return self.items[self.convert(index)]
    
    def append(self, item: Any) -> None:
        end = self.convert(len(self.items) - 1) + 1
        items = self.items
        left = items[:end]
        right = items[end:]
        self.items = left + [item] + right
        if self.head > 0:
            self.head += 1