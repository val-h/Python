lineOfNums = input('Line of integers: ')
arrNums = [int(x) for x in lineOfNums.split()]
minValue = min(arrNums)
maxValue = max(arrNums)
sumArr = sum(arrNums)
avgValue = sumArr / len(arrNums)
print(f'Min = {minValue}\nMax = {maxValue}\nSum = {sumArr}\nAverage = {avgValue}')