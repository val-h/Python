import sys
n = int(input('Number of elements: '))
sum = 0
maxNum = -sys.maxsize           # or max num = sys.float_info.min   / but you will have to cast other variables as int if you don't want decimal point
for i in range(1, n + 1):
    num = int(input(f'Value for the number {i}: '))
    sum += num
    maxNum = max(maxNum, num)
sum -= maxNum
if sum == maxNum:
    print(f'Yes! sum = {sum}')
else:
    print(f'No! diff = {abs(sum - maxNum)}')