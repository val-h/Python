deposits = int(input('Number of deposits: '))
accMoney = 0.0
cnt = 1
while cnt <= deposits:
    tmpDep = float(input('Add to the account: '))
    if tmpDep <= 0:
        print('Invalid operation!')
        break
    elif tmpDep > 0:
        accMoney += tmpDep
        print(f'Increase: {tmpDep}')
        cnt += 1
print(f'Total: {accMoney:.2f}')