from itertools import combinations
line_of_numbers = input('Line of numbers: ')

# Convert to int _ main thing
arr= [int(i) for i in line_of_numbers.split()]

# Get all of the combinations
psums = {sum(i):i for i in combinations(arr, 2)}

# Using only 1 for loop
for i, v in enumerate(arr):
    if v in psums:
        print(f'{psums[v][0]} + {psums[v][1]} == {v}')  # Not the exact type of solution i need
                                                        # But still it works nicely (gona use itertools in the future)
                                                                                                            