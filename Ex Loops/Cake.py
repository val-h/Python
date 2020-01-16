width = int(input('Width of the cake: '))
lenght = int(input('height of the cake: '))
totalCake = width * lenght
takenCake = 0
pieces = None
while totalCake >= takenCake:
    pieces = input('taken pieces: ')
    if pieces == 'STOP':
        break
    else:
        takenCake += int(pieces)
if totalCake >= takenCake:
    print(f'{totalCake - takenCake} pieces are left.')
else:
    print(f'No more cake left! {takenCake - totalCake}')