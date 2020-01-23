primeSum = 0
nonPrimeSum = 0

# Prime check function
def IsPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True

# Main Loop - going through commands/numbers
while True:
    usrInp = input('>> ')
    if usrInp == 'stop':
        break
    num = int(usrInp)
    if num < 0:
        print('Number is negative.')
    elif IsPrime(num) == True:
        primeSum += num
    else:
        nonPrimeSum += num

# Output
print(f'Sum of all prime numbers is: {primeSum}')
print(f'Sum of all non prime numbers is: {nonPrimeSum}')
