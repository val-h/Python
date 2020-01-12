totalSteps = 10000
stepsMoved = 0
while stepsMoved < totalSteps:
    usrI = input().lower()
    if usrI == 'going home':
        usrI = int(input())
        stepsMoved += usrI
        break
    else:
        stepsMoved += int(usrI)
if stepsMoved >= totalSteps:
    print('Goal reached!\nGood job!')
else:
    print(f'{totalSteps - stepsMoved} more steps to reach goal.')