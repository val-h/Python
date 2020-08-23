import threading
from threading import Semaphore
import time

def f1():
    x = 8192

    lock = threading.Lock()

    def double():
        global x, lock
        lock.acquire()
        while x < 16384:
            x *= 2
            print(x)
            time.sleep(1)
        print('Reached the maximum.')
        lock.release()

    def halve():
        global x, lock
        lock.acquire()
        while x > 1:
            x /= 2
            print(x)
            time.sleep(1)
        print('Reached the minimum.')
        lock.release()

    t1 = threading.Thread(target=halve)
    t2 = threading.Thread(target=double)

    t1.start()
    t2.start()

def f2():
    semaphore = threading.BoundedSemaphore(value=5)

    def access(thread_number):
        print(f'{thread_number} is trying to access!')
        semaphore.acquire()
        print(f'{thread_number} was granted access!')
        time.sleep(10)
        print(f'{thread_number} is now releasing!')
        semaphore.release()

    for thread_number in range(10):
        t = threading.Thread(target=access, args=(thread_number,))
        t.start()
        time.sleep(1)

f2()
