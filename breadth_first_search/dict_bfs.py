from collections import deque


def find_closest_mango_seller(friends: dict[str, list[str]]) -> str:
    search_queue = deque(friends['me'])
    searched: dict[str, bool] = {}
     
    while search_queue:
        friend = search_queue.popleft()       
        
        if searched.get(friend):
            continue
        
        if _is_mango_seller(friend):
            return friend
        
        search_queue += friends[friend]
        searched[friend] = True
        
    return 'no mango sellers'

    
def _is_mango_seller(name: str) -> bool:
    return name[-1] == 'm'