tables = int(input('Tables: '))
lenght = float(input('Lenght: '))
width = float(input('Width: '))

kSum = pow(lenght / 2, 2) * tables * 9
tSum = (lenght + 0.6) * (width + 0.6) * tables * 7
sum = tSum + kSum

print(f'{sum:.2f} USD')
print(f'{sum * 1.85:.2f} BGN')