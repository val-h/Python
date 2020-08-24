import threading
import time
from time import sleep

event = threading.Event()

def f1():
    def func():
        print('Waiting for event to trigger...')
        event.wait()
        print('Perfoming action.')

    t1 = threading.Thread(target=func)
    t1.start()

    x = input('Do you want to trigger the event?: ')

    if x == 'y':
        event.set()


def f2():
    path = 'Side scripts/text.txt'
    text = ''

    def readFile():
        nonlocal path, text
        while True:
            with open(path, 'r') as f:
                text = f.read()
            time.sleep(3)
    
    def print_loop():
        for x in range(30):
            print(text)
            time.sleep(1)
    t1 = threading.Thread(target=readFile, daemon=True)
    t2 = threading.Thread(target=print_loop)
    
    t1.start()
    t2.start()

f2()
