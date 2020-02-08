marketPrices = input('Jewels and gold prices: ')
pricesArr = [int(x) for x in marketPrices.split()]
totalEarnings = 0
totalExpenses = 0
arrCmd = []

while True:
    cmd = input('/> ')
    if cmd == 'Jail Time': break
    else:
        arrCmd = cmd.split()
        for c in arrCmd[0]:
            if c == '%':
                totalEarnings += pricesArr[0]   # Heist jewels
            elif c == '$':
                totalEarnings += pricesArr[1]   # Heist gold
        totalExpenses += int(arrCmd[1])         # Heist expenses)

if totalEarnings >= totalExpenses:
    print(f'Heists will continue. Total earnings: {totalEarnings - totalExpenses}.')
else:
    print(f'Have to find another job. Lost: {totalExpenses}.')
