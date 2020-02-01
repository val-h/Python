line_of_nums = input('Line of nums: ')
rotations = int(input('Rotation: '))
numArr = [int(x) for x in line_of_nums.split()]
rotatedSum = []

for i in range(0, rotations):
    lastDigit = numArr.pop()
    numArr.insert(0, lastDigit)
    if i == 0:
        rotatedSum = list(numArr)
    else:
        for q, x in enumerate(numArr):
            rotatedSum[q] += x
print(rotatedSum)
