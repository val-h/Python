lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]
specialNums = input('Bomb and magnitude number: ')
b, m = [int(x) for x in specialNums.split()]

while b in nums:
    indexB = nums.index(b)
    for r in range(indexB - m, indexB):
        if r >= 0:
            nums[r] = 0
    for r in range(indexB + 1, indexB + m + 1):
        if r < len(nums):
            nums[r] = 0
    nums[indexB] = 0

print(sum(nums))
