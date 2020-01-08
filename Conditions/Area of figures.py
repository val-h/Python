import math
figure = input('Type of figure: ').lower()
area = 0.0
if  figure == 'square':
    num = float(input('Side: '))
    area = num * num
elif figure == 'rectangle':
    num1 = float(input('Side 1: '))
    num2 = float(input('Side 2: '))
    area = num1 * num2
elif figure == 'circle':
    num1 = float(input('Rad: '))
    area = pow(num1, 2) * math.pi
elif figure == 'triangle':
    base = float(input('Base: '))
    h = float(input('h: '))
    area = base * h / 2
else:
    print('Invalid input!')
print(f'Area = {area:.3f}')