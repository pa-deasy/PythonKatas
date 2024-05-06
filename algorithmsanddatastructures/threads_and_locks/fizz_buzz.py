# 15.7 FizzBuzz: In the classic problem FizzBuzz, you are told to print the numbers from 1 to n. However when the number is divisible by 3, print "Fizz".
# When it is divisible by 5 print "Buzz". When it is divisible by 3 and 5 print "FizzBuzz". In this problem you are asked to do this in a multi-threaded way.
# Implement a multi-threaded version of FizzBuzz with four threads. One thread checks for divisibility of 3 and prints "Fizz". Another thread is responsible for 
# divisibility by 5 and prints "Buzz". A third thread is responsible for divisibility of 3 and 5 and prints "FizzBuzz". A fourth thread does the numbers.
from time import sleep
from threading import Semaphore


class FizzBuzz:
    limit: int
    number: Semaphore
    
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.number = Semaphore(1)
        
    def check_fizz(self) -> None:
        while self.number._value <= self.limit:
            if self.number._value % 3 == 0 and not self.number._value % 5 == 0:
                print('Fizz')
            sleep(1)
        
    def check_buzz(self) -> None:
        while self.number._value <= self.limit:
            if not self.number._value % 3 == 0 and self.number._value % 5 == 0:
                print('Buzz')
            sleep(1)
        
    def check_fizz_buzz(self) -> None:
        while self.number._value <= self.limit:
            if self.number._value % 3 == 0 and self.number._value % 5 == 0:
                print('FizzBuzz')
            sleep(1)
        
    def increment_number(self) -> None:
        while self.number._value <= self.limit:
            print(f'Number is {self.number._value}')
            sleep(2)
            self.number.release(1)