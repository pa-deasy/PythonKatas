from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    

@dataclass
class Position():
    y: int
    x: int
    path: list[Direction]
    maze: list[list[int]]
    
    def matches(self, other_position: 'Position'):
        return self.y == other_position.y and self.x == other_position.x
    
    def is_within_maze(self) -> bool:
        maze_size = len(self.maze) - 1
        return 0 <= self.y and self.y <= maze_size and 0 <= self.x and self.x <= maze_size
    
    def surrounding_positions(self) -> list['Position']:
        up = Position(x=self.x, y=self.y - 1, path=self.path + [Direction.UP], maze=self.maze)
        down = Position(x=self.x, y=self.y + 1, path=self.path + [Direction.DOWN], maze=self.maze)
        left = Position(x=self.x - 1, y=self.y, path=self.path + [Direction.LEFT], maze=self.maze)
        right = Position(x=self.x + 1, y=self.y, path=self.path + [Direction.RIGHT], maze=self.maze)
    
        surrounding_positions = [position for position in [up, down, left, right] if position.is_within_maze() and self.maze[position.y][position.x] == 1]
    
        return surrounding_positions
    
    
def all_possible_paths(maze: list[list[int]]) -> list[list[Direction]]:
    first_position = Position(x=0, y=0, path=[], maze=maze)
    target_position = Position(x=len(maze) - 1, y=len(maze) - 1, path=[], maze=maze)
    all_paths = _find_paths(first_position, [first_position], target_position)
    return all_paths
    
    
def _find_paths(position: Position, visited_positions: list[Position], target_position: Position) -> list[list[Direction]]:
    next_positions = position.surrounding_positions()
    
    found_paths = []
    for next in next_positions:
        if [v for v in visited_positions if v.matches(next)]:
            continue
        
        if next.matches(target_position):
            found_paths.append(next.path)
        else:
            newly_visited = visited_positions.copy()
            newly_visited.append(next)
            found_paths = found_paths + _find_paths(next, newly_visited, target_position)
    
    return found_paths

        