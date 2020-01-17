n = int(input('Enter the value for the total numbers: '))
oddSum = 0
evenSum = 0
for i in range(1 , n + 1):
    num = int(input(f'Enter a value for num in index {i}: '))
    if i % 2 == 0:
        evenSum += num
    else:
        oddSum += num
if oddSum == evenSum:
    print('Yes')
    print(f'Sum = {oddSum}')
else:
    print('No')
    print(f'Diff = {abs(oddSum - evenSum)}')