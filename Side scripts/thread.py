import threading
from time import sleep

def f1():
    def hello_world():
        while True:
            print('Hello, World!')

    def hello():
        while True:
            print('hello')

    t1 = threading.Thread(target=hello_world)
    t2 = threading.Thread(target=hello)

    t1.start()
    t2.start()

def f2():
    def function1():
        for x in range(1000):
            print('ONE')

    def function2():
        for x in range(1000):
            print('TWO')

    t1 = threading.Thread(target=function1)
    t2 = threading.Thread(target=function2)

    t1.start()
    t2.start()

def f3():
    def hello():
        for x in range(50):
            print('Hello')

    t1 = threading.Thread(target=hello)
    t1.start()

    t1.join()

f3()

print('Another text')
