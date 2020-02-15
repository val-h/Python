lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]

while True:
    cmd = input('/> ')
    if cmd == 'Odd':
        nums = [int(x) for x in nums if x % 2 != 0 ]
        break
    elif cmd == 'Even':
        nums = [int(x) for x in nums if x % 2 == 0]
        break
    else:
        uil = cmd.split()
        if uil[0] == 'Delete':
            nums = [v for v in nums if v != int(uil[1])]
        elif uil[0] == 'Insert':
            nums.insert(int(uil[2]), int(uil[1]))
        else:
            print(' - Error! - ')
print(nums)
