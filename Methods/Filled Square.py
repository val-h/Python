n = int(input('/> '))

def Line(n):
    for i in range(0, 2 * n):
        print('-', end='')
    print()

def MiddlePart(n):
    for q in range(0, n - 2):
        print('-', end='')
        for i in range(1, n):
            print('\\/', end='')
        print('-')

def FilledSquare(n):
    Line(n)
    MiddlePart(n)
    Line(n)

FilledSquare(n)
