name = input('Name: ')
cnt = 1
avgGrd = 0
failed = 0
excluded = False
while cnt <= 12:
    num = float(input(f'Grade {cnt}: '))
    if num < 4:
        failed += 1
        if failed == 2:
            excluded = True
            break
    else:
        cnt += 1
        avgGrd += num
avgGrd /= 12
if excluded == True:
    print(f'{name} has been excluded at {cnt} grade')
else:
    print(f'{name} graduated. Average grade: {avgGrd:.2f}')