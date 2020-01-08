x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

lenght = abs(x1 - x2)
width = abs(y1 - y2)

area = lenght * width
per = lenght * 2 + width * 2

print(f'area: {area:.2f} cm2')
print(f'perimeter: {per:.2f} cm')