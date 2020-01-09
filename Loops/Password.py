usn = input('Name: ')
psw = input('Password: ')

passInput = input('Enter your password: ')
while passInput != psw:
    print('Wrong password')
    passInput = input('Enter your password again: ')

print(f'Welcome {usn}!')

#asd