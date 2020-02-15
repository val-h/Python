lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]
lineOfSeq = input('Sequence: ')
seq = [int(x) for x in lineOfSeq.split()]
matched = False

for n in seq:
    if n in nums:
        matched = True
    else:
        matched = False
        break

if matched == True:
    print('YES!')
else:
    print('NO!')
