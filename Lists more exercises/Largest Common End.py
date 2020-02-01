arr1 = firstLine = input('First line: ').split()
arr2 = secondLine = input('Second line: ').split()
smallArr = min(len(arr1), len(arr2))
leftCount = 0
rightCount = 0

for i in range(0, smallArr):
    if arr1[i] == arr2[i]:
        leftCount += 1
    if arr1[-1 - i] == arr2[-1 - i]:
        rightCount += 1

print(max(leftCount, rightCount))
