lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]

def AddMany(arr):
    many = arr[1:]
    i = arr[0]
    for j in range(len(many) - 1, -1, - 1):
        nums.insert(i, many[j])

def Contains(x):
    for i, n in enumerate(nums):
        if x == n:
            return i
    else:
        return -1

def Shift(r):
    for i in range(0, r):
        nums.append(nums.pop(0))

def Pairs():
    for i in range(0, len(nums)):
        if i == len(nums):
            break
        nums[i] = nums[i] + nums[i + 1]
        nums.pop(i + 1)

while True:
    cmd = input('/> ')
    if cmd == 'print':
        break
    commandArr = cmd.split()
    commandNums = [int(x) for x in commandArr[1:]]
    if commandArr[0] == 'add':
        nums.insert(commandNums[0], commandNums[1])
    elif commandArr[0] == 'addMany':
        AddMany(commandNums)
    elif commandArr[0] == 'contains':
        Contains(commandNums[0])
    elif commandArr[0] == 'remove':
        nums.pop(commandNums[0])
    elif commandArr[0] == 'shift':
        Shift(commandNums[0])
    elif commandArr[0] == 'sumPairs':
        Pairs()

print(nums)
