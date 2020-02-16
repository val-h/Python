lineOfNums = input('Numbers: ')
nums = [int(x) for x in  lineOfNums.split()]

def NumReverse(x):
    x = str(x)
    x = x[::-1] # Start and end is left empty and adding a step of -1 reverses the string
    return int(x)

for i in range(0 , len(nums)):
    nums[i] = NumReverse(nums[i])
print(sum(nums))
