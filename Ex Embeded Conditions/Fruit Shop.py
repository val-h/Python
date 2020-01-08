fruit = input().lower()
day = input().lower()
qnt = float(input())

price = 0.0
error = bool(0)

if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    if fruit == 'banana':
        price = qnt * 2.5
    elif fruit == 'apple':
        price = qnt * 1.2
    elif fruit == 'orange':
        price = qnt * 0.85
    elif fruit == 'grapefruit':
        price = qnt * 1.45
    elif fruit == 'kiwi':
        price = qnt * 2.7
    elif fruit == 'pineapple':
        price = qnt * 5.5
    elif fruit == 'grapes':
        price = qnt * 3.85
    else:
        error = 1
elif day == 'saturday' or day == 'sunday':
    if fruit == 'banana':
        price = qnt * 2.7
    elif fruit == 'apple':
        price = qnt * 1.25
    elif fruit == 'orange':
        price = qnt * 0.90
    elif fruit == 'grapefruit':
        price = qnt * 1.60
    elif fruit == 'kiwi':
        price = qnt * 3
    elif fruit == 'pineapple':
        price = qnt * 5.6
    elif fruit == 'grapes':
        price = qnt * 4.2
    else:
        error = 1
else:
    error = 1

if error == 0:
    print(f'{price:.2f}lv.')
else:
    print('error')