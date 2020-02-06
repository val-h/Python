line_of_numbers = input('Input: ')
diff = int(input('Difference: '))
arrNums = [int(x) for x in line_of_numbers.split()]
pairsCount = 0

for i in range(0, len(arrNums)):
    for q in range(i + 1, len(arrNums)):
        if abs(arrNums[i] - arrNums[q]) == diff:
            pairsCount += 1
print(pairsCount)
