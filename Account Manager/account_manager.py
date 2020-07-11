import os
import json

from account import Account

def FindPath(f_name, path):
    for root, dirs, files in os.walk(path):
        if f_name in files:
            return os.path.join(root, f_name)

class AccountManager:
    """Acount Manager class with CRUD functionality."""

    q_cmds = {'quit', 'exit', 'terminate'}

    def __init__(self):
        """Initialize the account manager a load data from a json file."""
        # Dictionary to hold all the accounts and to load from
        filepath = FindPath('accounts.json', 'Account Manager')
        with open(filepath) as f:
            acc_dict = json.load(f)

        # Accounts dict
        self.accounts = acc_dict

        # Commands list
        self.commands = ['help', 'details', 'register', 'login', AccountManager.q_cmds]

        # Account logged in
        self.logged_acc = None

        # Command Line Interface
        print('Entering CLI...')
        self.CommandLine()

    def CommandLine(self):
        """Command line for the account manager with extra graphics."""
        prompt = '\n/> '
        while True:
            # Header part
            self._Header()
            
            # Main content
            self._Main()

            # Footer - Command input
            usr_inp = input(prompt)
            if usr_inp in AccountManager.q_cmds:
                print('Quiting...')
                quit()
            
            elif usr_inp in self.commands:
                if usr_inp == 'help':
                    self.Help()
                elif usr_inp == 'details':
                    self.PrintDetails()
                elif usr_inp == 'register':
                    self.CreateAccount()
                elif usr_inp == 'login':
                    self.LogInAccount()
                
            else:
                print('Error! Command not recognised.'
                '\nTry "help" for more info.')

    def _Header(self):
        """Header line for the CLI."""
        txt_line = 'Account Manager\t'
        if self.logged_acc == True:
            #txt_line += f'Username: {}'    
            pass
        txt_line += 'Login/Create Acc'
        print(txt_line)
    
    def _Main(self):
        """Main content for the CLI."""
        print(f'|\t\tDetails\t\t|')
        print(f'|\t\t       \t\t|')
        print(f'|\t\t       \t\t|')
        print(f'|\t\t-------\t\t|')

    def Help(self):
        """Help Function to print info about each command."""
        print('List of commands: ')
        for item in self.commands:
            print('\t-', item)

    def PrintDetails(self):
        """Print details about the current state of the Account Manager."""
        print('Totals accounts: ', len(self.accounts))

#        for acc in self.accounts:
#            print(f"Username: {acc['username']}")
#            print(f"Password: {acc['password']}")
#            print(f"Email: {acc['email']}")

    def CreateAccount(self):
        """Creates an account."""
        # User details, this will have a lot more testing and functionality
        username = input('Username: ').strip()
        password = input('Password: ').strip()
        rpt_pass = input('Repeat Password: ').strip()
        while password != rpt_pass:
            print('Passwords do not match, please enter the password again.')
            rpt_pass = input('Repeat Password: ').strip()
        email = input('Email: ').strip()

        # Create the account
        new_acc = Account(username, password, email)

        # Add the account to the acc dict
        self.accounts[len(self.accounts)] = {
            'username': username,
            'password': password,
            'email': email,
        }

        # Store the account in json file
        with open('Account Manager\\accounts.json', 'w') as f:
            json.dump(self.accounts, f, indent=4)

    def LogInAccount(self):
        """Log in to an existing account."""
        print('Login Form -')
        usr = input('Username: ')
        for acc in self.accounts:
            if usr == acc['username']:
                pswd = input('Password: ')
                if pswd == acc['password']:
                    print('Succesful Login!')
                    logged = Account(acc['username'], acc['password'], acc['email'])
                    return logged

