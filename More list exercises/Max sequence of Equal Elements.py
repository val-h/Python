lineOfNumbers = input('Numbers: ')
nums = [int(x) for x in lineOfNumbers.split()]
longest = []
temp = [nums[0]]

for i in range(1, len(nums)):
    if nums[i] == nums [i - 1]:
        temp.append(nums[i])
    else:
        temp = [nums[i]]
    if len(temp) > len(longest):
        longest = list(temp)
print(longest)
