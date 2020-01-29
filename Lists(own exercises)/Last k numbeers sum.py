# Input
n = int(input('Value for n: '))
k = int(input('Value for k: '))

# Variables
seq = [1]
tempSum = 0
lineOfNums = ''

# Main logic...
while len(seq) < n:
    if len(seq) < k:
        tempSum = sum(seq)
    else:
        tempSum = sum(seq[-k:])
    seq.append(tempSum)

# Output
for i in seq:
    lineOfNums += f'{i} '
print(lineOfNums)   # works like a charm... after 10 failed attempts...
