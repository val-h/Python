lineOfNums = input('Integers: ')
nums = [int(x) for x in lineOfNums.split()]
i = 0
sum = 0

while True:
    sum += nums[i]
    if len(nums) - i > nums[i]:
        i += nums[i]
    elif i - nums[i] >= 0:
        i -= nums[i]
    else:
        break

print(sum)
