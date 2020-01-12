monReq = float(input('Money required for holiday: '))
money = float(input('Current balance: '))
daysInRow = 0
days = 0
while money < monReq:
    action = input('Spend or save: ').lower()
    amount = float(input('Amount: '))
    days += 1
    if action == 'spend':
        daysInRow += 1
        money -= amount
        if daysInRow == 5:
            break
        if money < 0:
            money = 0
    elif action == 'save':
        money += amount
        daysInRow = 0
if money >= monReq and daysInRow != 5:
    print(f'You saved the money for {days} days.')
else:
    print('You can\'t save the money.')
    print(f'{days}')