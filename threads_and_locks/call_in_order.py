# 15.5 - Suppose we have a class Foo with methods first(), second() and third(). The same instance of Foo will be passed to three different threads.
# ThreadA with call first, ThreadB will call second and ThreadC will call third. Design a mechanism to ensure first is called before second and second is called before third.
from time import sleep
from threading import Semaphore


class Foo:
    first_semaphore: Semaphore
    second_semaphore: Semaphore
    
    def __init__(self) -> None:
        self.first_semaphore = Semaphore(1)
        self.second_semaphore = Semaphore(1)
        self.first_semaphore.acquire()
        self.second_semaphore.acquire()
    
    def first(self):
        print('First has run')
        sleep(2)
        self.first_semaphore.release()
        
    def second(self):
        self.first_semaphore.acquire()
        self.first_semaphore.release()
        
        print('Second has run')
        sleep(2)
        self.second_semaphore.release()
        
    def third(self):
        self.second_semaphore.acquire()
        self.second_semaphore.release()
        
        print('Third has run')
    