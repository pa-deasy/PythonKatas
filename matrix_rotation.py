from dataclasses import dataclass


@dataclass
class Matrix:
    cells: list[list[int]]

    def rotate_90_anti_clockwise(self) -> None:
        print()