from dataclasses import dataclass
from typing import Protocol


@dataclass
class Fruit(Protocol):
    colour: str
    
    def pick(self) -> str:
        return f"Picked a {self.colour} fruit"
    
    
    def peel(self) -> str:
        return f"Peeled off a {self.colour} skin"
    

@dataclass
class Kiwi(Fruit):
    pass
    
    
@dataclass
class Apple():
    colour: str
    
    def pick(self) -> str:
        return f"Picked a shiny {self.colour} apple"
    
    def peel(self) -> str:
        return f"Peeled the shiny {self.colour} skin off an apple"
    

@dataclass
class Bananna():
    colour: str
    
    def pick(self) -> str:
        return f"Picked a curvy {self.colour} bananna"
    
    def peel(self) -> str:
        return f"Peeled the curvy {self.colour} skin off a bananna"
    