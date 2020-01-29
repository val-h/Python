numStr = input('Values for x and y: ')

# Assigning the values - really bad way of doing it
num = numStr.split(' ')
x = int(num[0])
y = int(num[1])
middle = int(x / 2)
pair = None

# Disgusting logic
if y == 0:
    pair = middle
elif y >= middle:
    pair = y
elif y < middle:
    pair = middle + y

print(pair)
# Doesn't work properly : 