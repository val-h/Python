usrInp = None
while True:
    usrInp = input('Enter a destination: ')
    if usrInp == 'End':
        break
    tripCost = int(input('Travel cost: '))
    while tripCost > 0:
        savedMoney = int(input('Money saved this time: '))
        tripCost -= savedMoney
    print(f'Going to {usrInp}!')