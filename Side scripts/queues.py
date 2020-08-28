import queue

def q1():
    q = queue.Queue()

    numbers = [10, 20, 30, 40, 50, 60, 70]

    for number in numbers:
        q.put(number)

    print(q.get())

def q2():
    q = queue.LifoQueue()

    numbers = [1, 2, 3, 4, 5, 6, 7]

    for number in numbers:
        q.put(number)

    print(q.get())

def q3():
    q = queue.PriorityQueue()

    q.put((2, 'Hello World!'))
    q.put((11, 99))
    q.put((5, 7.5))
    q.put((1, True))

    while not q.empty():
        print(q.get()[1]) # remove the tuple selector for the whole

q3()
