money = float(input('Amount of money: '))
dec = money
coins = 0
while money > 0.00:
    if money >= 2:
        money -= 2
    elif money >= 1:
        money -= 1
    elif money >= 0.5:
        money -= 0.5
    elif money >= 0.2:
        money -= 0.2
    elif money >= 0.1:
        money -= 0.1
    elif money >= 0.05:
        money -= 0.05
    elif money >= 0.02:
        money -= 0.02
    elif money >= 0.01:
        money -= 0.01
    coins += 1
    #todo finish this mess - old problem with floating point numbers : /
    print(money)
print(coins)