from dataclasses import dataclass
from datetime import datetime
from typing import List, Protocol


# 7.11 - File System: Explain the data structures and algorithms that you would use to design an in-memory file system.
class Entry(Protocol):
    path: str
    name: str
    updated_at: datetime
    
    def rename():
        return
    
    def delete():
        return
    
    def get_full_path():
        return


class File(Entry):
    content: str
    size: int
    

class Directory(Entry):
    contents: List[Entry]
    
    def number_of_files():
        return
    
    def add():
        return
    
    def remove():
        return