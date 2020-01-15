from decimal import *
getcontext().prec = 2
money = float(input('Amount of money: '))
p = int(money * 100)
numCoins = 0
while p > 0:
    if p >= 200:
        p -= 200
    elif p >= 100:
        p -= 100
    elif p >= 50:
        p -= 50
    elif p >= 20:
        p -= 20
    elif p >= 10:
        p -= 10
    elif p >= 5:
        p -= 5
    elif p >= 2:
        p -= 2
    elif p >= 1:
        p -= 1
    numCoins += 1
    print(p)
print(f'Number of coins: {numCoins}')
# at long long last... i could have done this alot faster : / ...