f = float(input('Fahrenheit: '))

def FtoC(f):
    return (f - 32) * 5 / 9

print(f'{FtoC(f):.2f}')
