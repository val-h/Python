line_of_numbers = input('Line of numbers: ')
arrNums = [int(x) for x in line_of_numbers.split()]
longestIncreasingSequence = ''
tempSeq = f'{arrNums[0]} '

for i in range(1, len(arrNums)):    # Almost the same as the previous one
    if arrNums[i - 1] == arrNums[i] - 1:    # Had a bug with this line but somehow it fixed itself dunno.
        tempSeq += f'{arrNums[i]} '
    else:
        tempSeq = f'{arrNums[i]} '
    if len(tempSeq) > len(longestIncreasingSequence):
        longestIncreasingSequence = tempSeq
print(longestIncreasingSequence)
