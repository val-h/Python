line_of_numbers = input('Line of numbers: ')
arrNums = [int(x) for x in line_of_numbers.split()]
longestEqualSequence = ''
tempSeq = f'{arrNums[0]} '

for i in range(1, len(arrNums)):        # Looping through arrNums starting at index 1
    if arrNums[i] == arrNums[i - 1]:    # If arrNums at index i == arrNums at the previou index
        tempSeq += f'{arrNums[i]} '     
    else:                               # If not tempSeq gets reset
        tempSeq = f'{arrNums[i]} '
    if len(tempSeq) > len(longestEqualSequence):    # If tempSeq is larger(by lenght)
        longestEqualSequence = tempSeq
# Quite the simple program yet it took me way too long and at first i tried a solution with 3 loops 
print(longestEqualSequence) # Then with 2... then i realized this is actually a no brainer...
