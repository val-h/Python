import sys
n = int(input('Numbers to compare: '))
minNum = sys.float_info.max
cnt = 0
while cnt < n:
    num = float(input('Number: '))
    if num < minNum:
        minNum = num
    cnt += 1
print(f'Lowest number: {minNum:.0f}')