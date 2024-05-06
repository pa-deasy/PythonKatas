from dataclasses import dataclass
from typing import List, Protocol


# Implement filter functionality given a parser that can parse args into any format
@dataclass
class File:
    name: str
    location: str
    size: int
    type: str


class Filter(Protocol):
    def filter(self, files: List[File]) -> List[File]:
        ...
        

class SizeLessThanFilter:
    max_size: int
    
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
    
    def filter(self, files: List[File]) -> List[File]:
        return [f for f in files if f.size < self.max_size]
    
    
class TypeFilter:
    type: str
    
    def __init__(self, type: str) -> None:
        self.type = type
        
    def filter(self, files: List[File]) -> List[File]:
        return [f for f in files if f.type == self.type]
        
        
def apply_filters(files: List[File], filters: List[Filter]) -> List[File]:
    for f in filters:
        files = f.filter(files)
        
    return files