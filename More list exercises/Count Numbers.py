lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]
freq = {}

for n in nums:
    if n not in freq:
        freq[n] = 1
    else:
        freq[n] += 1
for key in sorted(freq):
    print(f'{key} -> {freq[key]}')
