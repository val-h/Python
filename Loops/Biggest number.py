import sys
n = int(input('How many numbers do you want t ocompare? -  '))
cnt = 0
maxNum = sys.float_info.min
while cnt < n:
    tmpNum = int(input('Enter a number: '))
    if maxNum < tmpNum:
        maxNum = tmpNum
    cnt += 1
print(f'Max number - {maxNum:.0f}')