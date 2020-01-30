lineOfNums = input('Line of numbers: ') # User input: example - 4 2 6 8
arrNums = [int(x) for x in lineOfNums.split()]  # A lot better - thanks kind SO stranger!
conMet = False # Is the condition met at least once

for a in range(0, len(arrNums) - 1):
    for b in range(a + 1, len(arrNums)):
        for c in range(0, len(arrNums)):
            if arrNums[a] + arrNums[b] == arrNums[c]:
                print(f'{arrNums[a]} + {arrNums[b]} == {arrNums[c]}')
                conMet = True

if conMet == False: print('No')
