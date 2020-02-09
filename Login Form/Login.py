# First personal project in Python!
#
# I will make it more complex as time goes on.

# Variables
command = None

usernames = []
passwords = []
emails = []

# Functions
def CommandType():
    print('Type a command') # Add help
    while True:
        command = input('/> ').lower()
        if command == 'reg':    UserRegister()
        elif command == 'log':  
            if not usernames:   # Checkes if the list is empty
                print('Error. No registered users.')
                print('Try registering first.')
            else:
                UserLogin()
        elif command == 'help': Help()
        elif command == 'exit':
            Exit()
        else:
            print('Error. Unknown command.')
            print('Type help for commands list')
        print()

def UserLogin():
    print('|   ---   Login Form   ---   |')
    attempts = 0
    while attempts < 3:
        print('Username: ', end='')
        uName = input()
        print('Password: ', end='')
        uPass = input()
        if uName in usernames:
                i = usernames.index(uName)
                if uName == usernames[i] and uPass == passwords[i]:
                    print('Access granted!')
                    print()
                    UserProfile(i)
                    break
        else:
            attempts += 1
            print('Access denied!')
            print('Wrong Username or Password.')
            print(f'{attempts} failed attempts to log in.')
            print()
    if attempts == 3:
        print('Too many failed attempts...')
        Exit()

def UserRegister():
    print('|   ---   Register new user   ---   |')
    usernames.append(input('Username: '))
    passwords.append(input('Password: '))
    emails.append(input('Email: '))

def UserProfile(i):
    print(f'|   ---   {usernames[i]}\'s Profile   ---   |')
    print()
    print('Personal information:')
    print(f"Username - {usernames[i]}")
    print(f"Password - {passwords[i]}")
    print(f"Email - {emails[i]}")

def Help():
    print('|   ---  Commands List   ---   |')
    print('reg - Register a new user')
    print('log - Login Form')
    print('exit - Exits program')
    print('help - Shows list of commands')

def Exit():
    print('Quiting program...')
    exit()

# Main
CommandType()

