from enum import Enum


NUMBER_OF_BALLS = 3
CALCULATIONS_CACHE = []

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


def possible_arrangements(reds: int, greens: int, blues: int) -> int:
    max_range = max(reds, greens, blues) + 1
    
    _generate_cache(max_range)
    
    count = count_arrangements(reds, greens, blues, Color.RED) + count_arrangements(reds, greens, blues, Color.GREEN) + count_arrangements(reds, greens, blues, Color.BLUE)
    
    return count
    
    
def _generate_cache(max_range: int) -> None:
    for h in range(0, max_range):
        for i in range(0, max_range):
            green_list = []
            for j in range(0, max_range):
                blue_list = []
                for k in range(0, max_range):
                    color_list = []
                    for l in range(0, NUMBER_OF_BALLS):
                        color_list.append(-1)
                    blue_list.append(color_list)
                green_list.append(blue_list)
            CALCULATIONS_CACHE.append(green_list)


def count_arrangements(reds: int, greens: int, blues: int, last_ball: Color):
    if reds < 0 or greens < 0 or blues < 0:
        return 0
    
    if reds == 1 and greens == 0 and blues == 0 and last_ball == Color.RED:
        return 1
    
    if reds == 0 and greens == 1 and blues == 0 and last_ball == Color.GREEN:
        return 1
    
    if reds == 0 and greens == 0 and blues == 1 and last_ball == Color.BLUE:
        return 1
    
    if CALCULATIONS_CACHE[reds][greens][blues][last_ball.value] != -1:
        return CALCULATIONS_CACHE[reds][greens][blues][last_ball.value]
    
    if last_ball == Color.RED:
        CALCULATIONS_CACHE[reds][greens][blues][last_ball.value] = count_arrangements(reds - 1, greens, blues, Color.GREEN) + count_arrangements(reds - 1, greens, blues, Color.BLUE)


    if last_ball == Color.GREEN:
        CALCULATIONS_CACHE[reds][greens][blues][last_ball.value] = count_arrangements(reds, greens - 1, blues, Color.RED) + count_arrangements(reds, greens - 1, blues, Color.BLUE)
    
    if last_ball == Color.BLUE:
        CALCULATIONS_CACHE[reds][greens][blues][last_ball.value] = count_arrangements(reds, greens, blues - 1, Color.RED) + count_arrangements(reds, greens, blues - 1, Color.GREEN)
        
    return CALCULATIONS_CACHE[reds][greens][blues][last_ball.value]
