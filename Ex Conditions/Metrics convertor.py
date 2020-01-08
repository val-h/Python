num = float(input())
fUnit = input().lower()
sUnit = input().lower()

if fUnit == 'mm':
    num /= 1000
elif fUnit == 'cm':
    num /= 100

if sUnit == 'mm':
    num *= 1000
elif sUnit == 'cm':
    num *= 100

print(f'{num:.3f}')