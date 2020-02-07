lineOfNums = input('Line of nums: ')
arrNums = [int(x) for x in lineOfNums.split()]
occurrence = int(input('Number to occur: '))
lastOccurenceIndex = None
targetSum = 0

for i in range(0 , len(arrNums)):
    if arrNums[i] == occurrence:
        lastOccurenceIndex = int(i)

if lastOccurenceIndex == None:
    print('No occurrences were found!')
else:
    for i in range(0, lastOccurenceIndex):
        targetSum += arrNums[i]
    print(targetSum)
