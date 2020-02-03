n = int(input('End of array: '))

def IsPrime(num):
    if num == 2 or num == 3: return True
    if num < 2 or num % 2 == 0: return False
    if num < 9: return True
    if num % 3 == 0: return False
    r = int(num ** 0.5)
    k = 5
    while k <= r:
        if num % k == 0: return False
        if num % (k + 2) == 0: return False
        k+=6
    return True
    

for i in range(2, n + 1):
    if IsPrime(i) == True:
        print(i, end=' ')
