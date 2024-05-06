from threading import Lock
from time import sleep

# 15.3 - Dining Philosophers: In the famous dining philosophers problem, a bunch of philosophers are sitting around a circular table with one chopstick between each of them.
# A philosopher needs both chopsticks to eat, and always picks up the left chopstick before the right one. 
# A deadlock could potentiall occur if all the philosophers reached for the left chopstick at the same time.
# Using threads and locks, implement a simulation of the dining philosophers problem that prevents deadlocks.

class Chopstick:
    lock: Lock
    number: int
    
    def __init__(self, number: int) -> None:
        self.lock = Lock()
        self.number = number
    
    def take(self, name: str) -> bool:
        acquired = self.lock.acquire()
        if acquired:
            print(f'{name} took chopstick {self.number}')
        return acquired
    
    def put_back(self, name: str) -> None:
        self.lock.release()
        print(f'{name} Put back chopstick {self.number}')
            
            
class Philosopher:
    name: str
    left: Chopstick
    right: Chopstick
    
    def __init__(self, name: str, left: Chopstick, right: Chopstick) -> None:
        self.name = name
        self.left = left
        self.right = right
        
    def eat(self) -> None:
        eaten = False
        while not eaten:
            took_left = self.left.take(self.name)
            took_right = self.right.take(self.name)
            if took_left and took_right:
                eaten = True
                print(f'{self.name} has eaten with chopsticks {self.left.number} and {self.right.number}')
            if took_left:
                self.left.put_back(self.name)
            if took_right:
                self.right.put_back(self.name)
            sleep(1)
        