from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    left: Optional['Node']
    right: Optional['Node']
    value: int