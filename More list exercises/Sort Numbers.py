lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]
nums.sort()
print(nums)