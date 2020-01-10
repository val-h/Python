name = input('Name: ')
avgGrd = 0
cnt = 1
while cnt <= 12:
    num = float(input(f'Grade {cnt}: '))
    if num < 4:
        print('Repeating class')
        pass
    else:
        cnt += 1
        avgGrd += num
avgGrd /= 12
print(f'{name} graduated. Average grade: {avgGrd:.2f}')