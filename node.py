from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: 'Node'
    right: 'Node'