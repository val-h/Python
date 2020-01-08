city = input().lower()
sales = float(input())

error = bool(0)
comis = 0.0

if city == 'sofia':
    if 0 <= sales <= 500:
        comis = sales * .05
    elif sales <= 1000:
        comis = sales * .07
    elif sales <= 10000:
        comis = sales * .08
    elif sales > 10000:
        comis = sales * .12
    else:
        error = 1
elif city == 'varna':
    if 0 <= sales <= 500:
        comis = sales * .045
    elif sales <= 1000:
        comis = sales * .075
    elif sales <= 10000:
        comis = sales * .10
    elif sales > 10000:
        comis = sales * .13
    else:
        error = 1
elif city == 'plovdiv':
    if 0 <= sales <= 500:
        comis = sales * .055
    elif sales <= 1000:
        comis = sales * .08
    elif sales <= 10000:
        comis = sales * .12
    elif sales > 10000:
        comis = sales * .145
    else:
        error = 1
else:
    error = 1

if error == 0:
    print(f'{comis:.2f}')
else:
    print('Error')