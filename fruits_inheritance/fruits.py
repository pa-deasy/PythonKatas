class Fruit():
    colour: str
    
    def __init__(self, colour: str) -> None:
        self.colour = colour
    
    def pick(self) -> str:
        return f"Picked a {self.colour} fruit"
    
    
    def peel(self) -> str:
        return f"Peeled off a {self.colour} skin"
    

class Kiwi(Fruit):
    pass
    
    
class Apple(Fruit):
    def pick(self) -> str:
        return f"Picked a shiny {self.colour} apple"
    
    def peel(self) -> str:
        return f"Peeled the shiny {self.colour} skin off an apple"
    

class Bananna(Fruit):
    def pick(self) -> str:
        return f"Picked a curvy {self.colour} bananna"
    
    def peel(self) -> str:
        return f"Peeled the curvy {self.colour} skin off a bananna"
    