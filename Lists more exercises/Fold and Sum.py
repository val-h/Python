line_of_nums = input('Line of numbers: ')
originalArr = [int(x) for x in line_of_nums.split()]
oLen = len(originalArr)
foldArr = []

for i in range(0, int(oLen / 4)):
    popped = originalArr.pop(0)
    foldArr.append(popped)
foldArr.reverse()
for i in range(0, int(oLen / 4)):
    popped = originalArr.pop()
    foldArr.append(popped)
print(oLen)
for i in range(0, len(originalArr)): # If len(originalArr) is replaced with oLen it gives an error(No idea why)
    originalArr[i] = originalArr[i] + foldArr[i]

print(originalArr)
