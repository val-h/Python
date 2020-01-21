usrInp = None
while True:
    usrInp = input('Enter a destination: ')
    if usrInp == 'End':
        break
    tripCost = int(input('Travel cost: '))
    while tripCost > 0:
        savedMoney = int(input('Money saved this time: '))
        tripCost -= savedMoney  # The time i discovered i should end text files with a new line
    print(f'Going to {usrInp}!') # https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline
