lineOfNumbers = input('Numbers: ')
multipleLists = lineOfNumbers.split('|')
nums = []
for i in range(0, len(multipleLists)):
    nums.extend(multipleLists[i].split())
print(nums)
