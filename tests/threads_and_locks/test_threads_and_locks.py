import threading
from threads_and_locks.dining_philosophers import Chopstick, Philosopher


def test_eat_when_many_philosophers_eating_then_prevents_deadlock():
    chopstick_ab = Chopstick(1)
    chopstick_bc = Chopstick(2)
    chopstick_cd = Chopstick(3)
    chopstick_de = Chopstick(4)
    chopstick_ea = Chopstick(5)
    
    philosopher_a = Philosopher('Patick', chopstick_ea, chopstick_ab)
    philosopher_b = Philosopher('Nicole', chopstick_ab, chopstick_bc)
    philosopher_c = Philosopher('Adam', chopstick_bc, chopstick_cd)
    philosopher_d = Philosopher('Paddy', chopstick_cd, chopstick_de)
    philosopher_e = Philosopher('Adrian', chopstick_de, chopstick_ea)
    
    thread_a = threading.Thread(target=philosopher_a.eat)
    thread_b = threading.Thread(target=philosopher_b.eat)
    thread_c = threading.Thread(target=philosopher_c.eat)
    thread_d = threading.Thread(target=philosopher_d.eat)
    thread_e = threading.Thread(target=philosopher_e.eat)
    
    thread_a.start()
    thread_b.start()
    thread_c.start()
    thread_d.start()
    thread_e.start()