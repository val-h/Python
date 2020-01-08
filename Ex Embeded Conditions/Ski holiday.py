days = int(input())
room = input().lower()
review = input().lower()
days -= 1
price = 0.0
error = bool(0)
if room == 'room for one person':
    if 0 < days:
        price = days * 18
elif room == 'apartment':
    if 0 < days < 10:
        price = days * 25 - (days * 25 * .3)
    elif days < 15:
        price = days * 25 - (days * 25 * .35)
    elif days > 15:
        price = days * 25 - (days * 25 * .5)
    else:
        error = 1
elif room == 'president apartment':
    if 0 < days < 10:
        price = days * 35 - (days * 35 * .1)
    elif days < 15:
        price = days * 35 - (days * 35 * .15)
    elif days > 15:
        price = days * 35 - (days * 35 * .20)
    else:
        error = 1
else:
    error = 1
if review == 'positive':
    price += price * .25
elif review == 'negative':
    price -= price * .1
else:
    error = 1
if error == 0:
    print(f'{price:.2f}')
else:
    print('Error')