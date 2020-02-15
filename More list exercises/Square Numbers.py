import math
lineOfNums = input('Numbers: ')
nums = [int(x) for x in lineOfNums.split()]
squares = []

for n in nums:
    if math.sqrt(n) == int(math.sqrt(n)):
        squares.append(n)
squares.sort(reverse=True)
print(squares)
