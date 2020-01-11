width = int(input('Width: '))
lenght = int(input('Lenght: '))
height = int(input('Height: '))
kubM = width * lenght * height
usr = None
while kubM >= 0:
    usr = input().lower()
    if usr == 'done':
        break
    else:
        kubM -= int(usr)
if kubM >= 0:
    print(f'{kubM} Cubic meters left.')
else:
    print(f'No more free space! You need 2 Cubic meters more.')