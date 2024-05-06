from threads_and_locks.call_in_order import Foo
from threading import Thread


def test_foo_when_first_second_third_executed_then_run_in_correct_order():
    foo = Foo()
    
    thread_a = Thread(target=foo.first)
    thread_b = Thread(target=foo.second)
    thread_c = Thread(target=foo.third)
    
    thread_c.start()
    thread_b.start()
    thread_a.start()