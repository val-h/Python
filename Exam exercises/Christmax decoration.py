budget = int(input('Family budget: '))
while budget > 0:
    usrInp = input('Decoration: ')
    if usrInp == 'Stop':
        print(f'Money left: {budget}')
        break
    wordSum = 0
    for c in usrInp:
        wordSum += ord(c)
    if budget >= wordSum:
        budget -= wordSum
        print(f'Item successfully purchased!')
    else:
        print(f'Not enough money!')
        break
