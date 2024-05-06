from threading import Thread
from threads_and_locks.fizz_buzz import FizzBuzz


def test_fizz_buzz_when_number_is_incremented_then_correct_output_printed():
    fizz_buzz = FizzBuzz(15)
    
    thread_fizz = Thread(target=fizz_buzz.check_fizz)
    thread_buzz = Thread(target=fizz_buzz.check_buzz)
    thread_fizz_buzz = Thread(target=fizz_buzz.check_fizz_buzz)
    thread_numbers = Thread(target=fizz_buzz.increment_number)
    
    thread_fizz.start()
    thread_buzz.start()
    thread_fizz_buzz.start()
    thread_numbers.start()
    