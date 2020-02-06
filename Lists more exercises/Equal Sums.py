lineOfNums = input('Line of nums: ')
arrNums = [int(x) for x in lineOfNums.split()]

for i in range(0, len(arrNums)):
    leftSum = 0
    rightSum = 0
    for q in range(0, i):
        leftSum += arrNums[q]
    for j in range(i + 1, len(arrNums)):
        rightSum += arrNums[j]
    if leftSum == rightSum:
        print(f'Middle ground at index: {i}')
        break
else:
    print('no')
