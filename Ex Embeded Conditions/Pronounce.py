age = int(input('Age: '))
gender = input('Gender: ')
error = False
if age >= 16:
    if gender == 'm':
        print('Mr.')
    elif gender == 'f':
        print('Ms.')
    else:
        print('Error')
elif age < 16:
    if gender == 'm':
        print('Master')
    elif gender == 'f':
        print('Miss')
    else:
        print('Error')