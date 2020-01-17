import sys
n = int(input('Numbers to calculate: '))
numMax = sys.float_info.min
numMin = sys.float_info.max
for i in range(1 , n+1):
    num = int(input(f'Please enter the value for {i}: '))
    numMin = int(min(num, numMin))
    numMax = int(max(num, numMax))
print(f'Max number: {numMax}')
print(f'Min number: {numMin}')