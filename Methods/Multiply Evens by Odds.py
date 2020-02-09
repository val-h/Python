n = input('Number: ')
arrNum = [int(x) for x in n]
oddSum = 0
evenSum = 0

for i in arrNum:
    if i % 2 != 0:
        oddSum += i
    else:
        evenSum += i

print(f'The sum of even digits - {evenSum} times the sum of odd digits - {oddSum} is equal to: {evenSum * oddSum}')
