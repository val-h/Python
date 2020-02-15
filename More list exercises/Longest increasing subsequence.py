lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]
longest = [1]
sequences = [str(x) for x in nums]  # looks better than lineOfNums.split()

for i in range(1, len(nums)):   # First loop to go through every single element in the arr
    for j in range(0, i):       # Second loop to go through every element before i
        if nums[i] > nums[j]:
            if len(sequences[i]) < len(sequences[j]) + 1:   # making sure the leftmost seq is stored
                sequences[i] = f'{sequences[j]} {nums[i]}'  # Assigning the new bigger sequence
    if len(sequences[i]) > len(longest):
        longest = sequences[i]  # Assigning the longest sequence
print(longest)
