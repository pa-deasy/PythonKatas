from dataclasses import dataclass
from typing import Optional


@dataclass
class Box():
    has_key: bool
    description: str
    contained_boxes: list['Box']
    

def search_for_key(box: Box) -> Optional[Box]:
    if box.has_key:
        return box
    
    for box in box.contained_boxes:
        return search_for_key(box)
        