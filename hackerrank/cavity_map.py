def mark_cavities(raw_grid: list[str]) -> list[str]:
    grid = Grid(raw_grid)

    marked_cavities = grid.mark_cavitites()

    return marked_cavities


class Grid:
    cells: list[list[int]]
    
    def __init__(self, raw_grid: list[str]):
        self.cells = []
        for raw_row in raw_grid:
            row = [int(digit) for digit in raw_row]
            self.cells.append(row)
            
    def _above(self, y: int, x: int) -> int:
        return self.cells[y - 1][x]
    
    def _below(self, y: int, x: int) -> int:
        return self.cells[y + 1][x]
    
    def _left(self, y: int, x: int) -> int:
        return self.cells[y][x - 1]
    
    def _right(self, y: int, x: int) -> int:
        return self.cells[y][x + 1]
    
    def _surrounded_by_smaller_cells(self, y: int, x: int) -> bool:
        value = self.cells[y][x]
        return self._above(y, x) < value and self._below(y, x) < value and self._left(y, x) < value and self._right(y, x) < value 
    
    def _position_on_border(self, y:int, x:int) -> bool:
        if y == 0 or y == len(self.cells) - 1 or x == 0 or x == len(self.cells[0]) - 1:
            return True
        else:
            return False
        
    def _is_cavity(self, y: int, x: int) -> bool:
        return not(self._position_on_border(y, x)) and self._surrounded_by_smaller_cells(y, x)
    
    def mark_cavitites(self) -> list[str]:
        marked: list[str] = []
        for y_index in range(len(self.cells)):
            marked_row: list[str] = []
            row = self.cells[y_index]
            for x_index in range(len(row)):
                if self._is_cavity(y_index, x_index):
                    marked_row.append('X')
                else:
                    marked_row.append(str(self.cells[y_index][x_index]))
            marked.append(''.join(marked_row))
            
        return marked
