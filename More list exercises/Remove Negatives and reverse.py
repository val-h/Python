lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]
positiveNums = []

for i in range(0, len(nums)):
    if nums[i] >= 0:
        positiveNums.append(nums[i])
positiveNums.reverse()
if not positiveNums:
    print('empty')
else:
    print(positiveNums)
