n = int(input('Lenght of the array: '))
nums = []
for i in range(0, n):
    nums.append(int(input(f'Enter the value for element at index {i + 1}: ')))
nums.reverse()
lineOfNums = ''
for i in nums:
    lineOfNums += f'{i} '
print(lineOfNums)