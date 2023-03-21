def save_the_prisoner(prisoner_count: int, candy_count: int, starting_chair: int) -> int:
    chair = (candy_count + (starting_chair - 1)) % prisoner_count
    
    return prisoner_count if chair == 0 else chair
    
    # current_chair = starting_chair
    # for candy_index in range(candy_count - 1):
    #     if current_chair == prisoner_count:
    #         current_chair = 1
    #     else:
    #         current_chair += 1
    
    # return current_chair



   
# (4, 6, 2) -> 3
# 2 3 4 1 2 3