from dataclasses import dataclass


@dataclass
class Matrix:
    cells: list[list[int]]

    def rotate_90_anti_clockwise(self) -> None:
        rotated_cells: list[list[int]] = []
        
        for column_index in range(len(self.cells) - 1, -1, -1):
            rotated_row: list[int] = []
            for row_index in range(0, len(self.cells)):
                rotated_row.append(self.cells[row_index][column_index])
            rotated_cells.append(rotated_row)
            
        self.cells = rotated_cells
