n = int(input('Enter the total numbers for Left and Right side: '))
leftSum = 0
rightSum = 0
for i in range(1, n +1 ):
    num = int(input(f'Enter a value for Left Sum in index {i}: '))
    leftSum+= num
for j in range(1 , n +1):
    num = int(input(f'Enter a value for Right Sum in index {j}: '))
    rightSum += num
if leftSum == rightSum:
    print(f'Yes, sum = {leftSum}')
else:
    print(f'No, diff = {abs(leftSum - rightSum)}')