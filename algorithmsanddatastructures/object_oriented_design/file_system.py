from dataclasses import dataclass
from typing import List


# 7.11 - File System: Explain the data structures and algorithms that you would use to design an in-memory file system.
@dataclass
class Entry:
    name: str
    parent: 'Directory'


@dataclass
class File(Entry):
    size: int


@dataclass
class Directory(Entry):
    entries: List[Entry]

    def add_entries(self, entries: List[Entry]) -> None:
        self.entries += entries

    def number_of_files(self) -> int:
        count = 0

        for entry in self.entries:
            if isinstance(entry, Directory):
                count += 1
                count += entry.number_of_files()
            elif isinstance(entry, File):
                count += 1

        return count