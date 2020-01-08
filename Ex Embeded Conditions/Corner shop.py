product = input().lower()
city = input().lower()
quantity = float(input())
total = 0.0
error = bool(0)

if city == 'sofia':
    if product == 'coffee':
        total = quantity * 0.5
    elif product == 'water':
        total = quantity * 0.8
    elif product == 'beer':
        total = quantity * 1.2
    elif product == 'sweets':
        total = quantity * 1.45
    elif product == 'peanuts':
        total = quantity * 1.6
    else:
        error = 1
elif city == 'plovdiv':
    if product == 'coffee':
        total = quantity * 0.4
    elif product == 'water':
        total = quantity * 0.7
    elif product == 'beer':
        total = quantity * 1.15
    elif product == 'sweets':
        total = quantity * 1.30
    elif product == 'peanuts':
        total = quantity * 1.5
    else:
        error = 1
elif city == 'varna':
    if product == 'coffee':
        total = quantity * 0.45
    elif product == 'water':
        total = quantity * 0.7
    elif product == 'beer':
        total = quantity * 1.1
    elif product == 'sweets':
        total = quantity * 1.35
    elif product == 'peanuts':
        total = quantity * 1.55
    else:
        error = 1
else:
    error = 1

if error == 1:
    print('Error')
else:
    print(f'{total:.2f}lv.')