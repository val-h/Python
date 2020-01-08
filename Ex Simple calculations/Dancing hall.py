l = float(input('l = '))
w = float(input('w = '))
a = float(input('a = '))

area = (l * 100) * (w * 100)
wd = pow(a * 100, 2)
bench = area / 10
freeSpace = area - bench - wd

spaceLeft = freeSpace / (40 + 7000)
print(round(spaceLeft))