numStr = input('Values for x and y: ')
num = [int(x) for x in numStr.split()]
x, y = num
middle = int(x / 2)
pair = None

# Disgusting logic
if y == 0:
    pair = middle
elif y >= middle:
    pair = middle - y
elif y < middle:
    pair = middle + y

print(pair) # Works perfectly now
