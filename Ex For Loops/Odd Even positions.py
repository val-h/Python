import sys
n = int(input('Number of elements: '))
oddSum = 0.0
oddMin = sys.maxsize
oddMax = -sys.maxsize
evenSum = 0.0
evenMin = sys.maxsize
evenMax = -sys.maxsize
for i in range(1, n + 1):
    num = float(input(f'Enter a value for element in the index {i}: '))
    if i % 2 != 0:
        oddSum += num
        oddMin = min(oddMin, num)
        oddMax = max(oddMax, num)
    else:
        evenSum += num
        evenMin = min(evenMin, num)
        evenMax = max(evenMax, num)

# Output
print(f'OddSum={oddSum:.2f},')
if oddMin == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={oddMin:.2f}')
if oddMax == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={oddMax:.2f},')
print(f'EvenSum={evenSum:.2f},')
if evenMin == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={evenMin:.2f},')
if evenMax == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={evenMax:.2f}')