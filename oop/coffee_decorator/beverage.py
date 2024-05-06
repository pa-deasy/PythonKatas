from enum import Enum


class Size(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'


class Beverage:
    size: Size
    description: str
    
    def __init__(self, size: Size) -> None:
        self.size = size
        self.description = 'Unknown beverage'
    
    def get_description(self) -> str:
        return self.description
    
    def get_size(self) -> Size:
        return self.size
    
    def cost(self) -> float:
        ...
        
        
class DarkRoast(Beverage):
    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = 'Dark Roast'
    
    def cost(self) -> float:
        cost = 3
        match self.size:
            case Size.SMALL:
                cost = 3
            case Size.MEDIUM:
                cost = 4
            case Size.LARGE:
                cost = 5
        return cost
    

class HomeBlend(Beverage):
    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = 'Home Blend'
    
    def cost(self) -> float:
        cost = 2.50
        match self.size:
            case Size.SMALL:
                cost = 2.50
            case Size.MEDIUM:
                cost = 3.50
            case Size.LARGE:
                cost = 4.50
        return cost
    
    
class CondimentDecorator(Beverage):
    beverage: Beverage
    
    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage
    
    def get_size(self) -> Size:
        return self.beverage.get_size()
    
    def get_description(self) -> str:
        ...
        
        
class Milk(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ', Milk'
    
    def cost(self) -> float:
        cost = 0
        match self.beverage.get_size():
            case Size.SMALL:
                cost = .1
            case Size.MEDIUM:
                cost = .2
            case Size.LARGE:
                cost = .3
        return self.beverage.cost() + cost
    

class Mocha(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ', Mocha'
    
    def cost(self) -> float:
        cost = 0
        match self.beverage.get_size():
            case Size.SMALL:
                cost = .2
            case Size.MEDIUM:
                cost = .3
            case Size.LARGE:
                cost = .4
        return self.beverage.cost() + cost
        