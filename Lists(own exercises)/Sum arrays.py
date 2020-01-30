firstListOfNums = input('First list of nums: ')
secondListOfNums = input('Second list of nums: ')
arr1 = [int(x) for x in firstListOfNums.split()]
arr2 = [int(x) for x in secondListOfNums.split()]
longArr = []
shortArr = []

if len(arr1) >= len(arr2):
    longArr = arr1
    shortArr = arr2
else:
    longArr = arr2
    shortArr = arr1

for i in range(0, len(longArr)):
    print(longArr[i] + shortArr[i % len(shortArr)]) # Actually works need to check it out later
    