from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int
    steps_traveled: int
    
    def matches(self, other_position: 'Position'):
        return self.x == other_position.x and self.y == other_position.y
    
    def is_within_maze(self, maze_size: int) -> bool:
        return 0 <= self.x and self.x <= maze_size and 0 <= self.y and self.y <= maze_size
    
    def surrounding_positions(self, maze_size: int) -> list['Position']:
        up = Position(x=self.x, y=self.y - 1, steps_traveled=self.steps_traveled + 1)
        down = Position(x=self.x, y=self.y + 1, steps_traveled=self.steps_traveled + 1)
        left = Position(x=self.x - 1, y=self.y, steps_traveled=self.steps_traveled + 1)
        right = Position(x=self.x + 1, y=self.y, steps_traveled=self.steps_traveled + 1)
    
        surrounding_positions = [position for position in [up, down, left, right] if position.is_within_maze(maze_size)]
    
        return surrounding_positions
    

def quickest_path(maze: list[list[int]]) -> int:
    maze_size = len(maze) - 1
    start = Position(x=0, y=0, steps_traveled=0)
    finish = Position(x=maze_size, y=maze_size, steps_traveled=0)
    
    visited_positions: list[Position] = []
    position_queue: list[Position] = [start]
    
    while position_queue:
        current_position = position_queue.pop(0)
        if [visited for visited in visited_positions if visited.matches(current_position)]:
            continue
        
        if current_position.matches(finish):
            return current_position.steps_traveled
        
        surrounding_positions = current_position.surrounding_positions(maze_size)
        unblocked_surrounding_positions = [position for position in surrounding_positions if maze[position.x][position.y] == 1]
        
        position_queue += unblocked_surrounding_positions
        visited_positions.append(current_position)
    
    return 0
