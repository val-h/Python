n = int(input())

def UpperTriangle(n):
    for i in range(1, n + 1):
        for q in range(1, i + 1):
            print(q, end=' ')
        print()

def BottomTriangle(n):
    for i in range(n - 1, 0, -1):
        for q in range(1, i + 1):
            print(q, end=' ')
        print()

def Triangle(n):
    UpperTriangle(n)
    BottomTriangle(n)

Triangle(n)
