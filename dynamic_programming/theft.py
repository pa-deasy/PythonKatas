from dataclasses import dataclass


@dataclass
class StealableItem:
    name: str
    value: int
    weight: int


def calculate_maximum_profit(items: list[StealableItem], bag_size: int) -> int:
    grid = _generate_grid(items, bag_size)
    
    for item_index in range(len(items)):
        item = items[item_index]
        for weight_index in range(bag_size):
            weight = weight_index + 1
            
            previous_max = grid[item_index - 1][weight_index] if item_index - 1 >= 0 else 0
            
            current_max = item.value if item.weight <= weight else 0
                
            if item_index - 1 >= 0 and weight_index - item.weight >= 0:
                current_max += grid[item_index - 1][weight_index - item.weight]
                
            grid[item_index][weight_index] = max(previous_max, current_max)
            
    return grid[len(items) -1][bag_size - 1]
            
    
def _generate_grid(items: list[int], bag_size: int) -> list[list[int]]:
    grid = []
    for index in range(len(items)):
        grid_line = []
        for index in range(bag_size):
            grid_line.append(0)
        grid.append(grid_line)
        
    return grid
    