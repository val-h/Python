# First personal project in Python!
#
# I will make it more complex as time goes on.

# Variables
command = None
userData = {
    'username': None,
    'password': None,
    'email': None
}

# Functions
def CommandType():
    print('Type a command') # Add help
    while True:
        command = input('\> ').lower()
        if command == 'reg':    UserRegister()
        elif command == 'log':  
            if userData['username'] == None:
                print('Error. No registered users.')
                print('Try registering first.')
            else:
                UserLogin()
        elif command == 'help': Help()
        elif command == 'exit':
            print('Quiting program...')
            exit()
        else:
            print('Error. Unknown command.')
            print('Type help for commands list')
            print()

def UserLogin():
    print('|   ---   Login Form   ---   |') #TODO add number of tries -> 3 max
    while True:
        print('Username: ', end='')
        uName = input()
        print('Password: ', end='')
        uPass = input()
        if uName == userData['username'] and uPass == userData['password']:
            print('Access granted!')
            print()
            UserProfile()
        else:
            print('Access denied!')
            print('Wrong Username or Password.')
            print()
            # availableTries -= 1

def UserRegister():
    print('|   ---   Register new user   ---   |')
    userData['username'] = input('Username: ')
    userData['password'] = input('Password: ')
    userData['email'] = input('Email: ')
    print()

def UserProfile():
    print('|   ---   User Profile   ---   |')
    print()
    print('Personal information:')
    print(f"Username - {userData['username']}")
    print(f"Password - {userData['password']}")
    print(f"Email - {userData['email']}")
    print()
    CommandType()

def Help():
    print('|   ---  Commands List   ---   |')
    print('reg - Register a new user')
    print('log - Login Form')
    print('exit - Exits program')
    print('help - Shows list of commands')
    print()

# Main
CommandType()

