EMPTY_CELL = '_'

def are_ladybugs_happy(ladybugs_board: str) -> str:
    ladybugs_count = _get_ladybugs_count(ladybugs_board)
    
    if _has_only_empty_cells(ladybugs_count):
        return 'YES'
    elif _has_lonely_ladybug(ladybugs_count):
        return 'NO'
    elif _can_make_ladybugs_happy(ladybugs_count):
        return 'YES'
    elif _has_one_ladybug(ladybugs_count):
        return 'YES'
    else:
        return 'NO'


def _get_ladybugs_count(ladybugs_board: str) -> dict[str, int]:
    ladybugs_count: dict[str, int] = {}
    ladybugs = list(ladybugs_board)
    for ladybug in ladybugs:
        ladybug_count = ladybugs_count.get(ladybug)
        if ladybug_count:
            ladybugs_count[ladybug] = ladybug_count + 1
        else:
            ladybugs_count[ladybug] = 1
    return ladybugs_count


def _has_only_empty_cells(ladybugs_count: dict[str, int]) -> bool:
    if len(ladybugs_count) == 1 and ladybugs_count.get(EMPTY_CELL):
        return True
    
def _has_lonely_ladybug(ladybugs_count: dict[str, int]) -> bool:
    for key, value in ladybugs_count.items():
        if key != EMPTY_CELL and value == 1:
            return True
    return False

def _has_one_ladybug(ladybugs_count: dict[str, int]) -> bool:
    has_empty_cell = ladybugs_count.get(EMPTY_CELL)
    if has_empty_cell:
        return len(ladybugs_count) - 1 == 1
    else:
        return len(ladybugs_count) == 1
    
    
def _can_make_ladybugs_happy(ladybugs_count: dict[str, int]) -> bool:
    empty_cell_count = ladybugs_count.get(EMPTY_CELL, 0)
    if empty_cell_count >=1:
        return True
