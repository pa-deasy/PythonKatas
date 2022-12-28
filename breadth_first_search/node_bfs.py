from collections import deque
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    is_mango_seller: bool
    friends: list['Person']


def find_closest_mango_seller(me: Person) -> str:
    search_queue = deque(me.friends)
    searched: dict[str, bool] = {}
     
    while search_queue:
        friend = search_queue.popleft()       
        
        if searched.get(friend.name):
            continue
        
        if friend.is_mango_seller:
            return friend.name
        
        search_queue += friend.friends
        searched[friend.name] = True
        
    return 'no mango sellers'
