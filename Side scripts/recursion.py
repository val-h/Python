# Factorial with recursion
n = int(input('Enter a factorial number: '))

def non_recursive(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1

    print(fact)

def recursive(n):
    if n < 1:
        return 1
    else:
        number = n * recursive(n-1)
        return number

non_recursive(n)
print(recursive(n))