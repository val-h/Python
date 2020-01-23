def IsPrime(n):
    if n == 2 or n == 3: return True
    if n<2 or n%2 == 0: return False
    if n<9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True

num = 2
while num < 10000000:
    if IsPrime(num) == True: print(num)
    num += 1