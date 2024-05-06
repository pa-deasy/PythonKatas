from enum import Enum
from typing import Protocol


class Pokemon(Protocol):
    def selected(self) -> str:
        ...
        
        
class Squirtle:
    def selected(self) -> str:
        return 'Select Squirtle a water type Pokemon that is sure to make a splash'
    
    
class Charmander:
    def selected(self) -> str:
        return 'Selected Charmander a fire type Pokemon with a sparky personality'
    
    
class Bulbasaur:
    def selected(self) -> str:
        return 'Selected Bulbasaur a grass type Pokemeon that is cool as a breeze'
    
    
class Type(Enum):
    WATER = 'water'
    FIRE = 'fire'
    GRASS = 'grass'
    

class PokemonFactory:
    def choose(type: Type) -> Pokemon:
        match type:
            case Type.WATER:
                return Squirtle()
            case Type.FIRE:
                return Charmander()
            case Type.GRASS:
                return Bulbasaur()