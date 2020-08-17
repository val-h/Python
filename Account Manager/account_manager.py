from os import path
from pathlib import Path
import json

from account import Account

# Find the base dir for the container folder (Account Manager)
BASE_DIR = Path(__file__).resolve(strict=True).parent

class AccountManager:
    """Acount Manager class with CRUD functionality."""

    q_cmds = {'quit', 'exit', 'terminate'}

    def __init__(self):
        """Initialize the account manager a load data from a json file."""
        # Dictionary to hold all the accounts and to load from
        self.acc_filepath = path.join(BASE_DIR, 'accounts.json')
        print(self.acc_filepath)
        with open(self.acc_filepath) as f:
            acc_dict = json.load(f)
            print(acc_dict)

        # Accounts dict
        self.accounts = acc_dict
        print(self.accounts)

        # Commands list
        self.commands = [
            'help',
            'details',
            'register',
            'login',

            # Quit commands
            AccountManager.q_cmds
            ]

        self.user_commands = [
            'logout',
            
        ]

        # Account logged in
        self.logged_acc = None

    def CommandLine(self):
        """Command line for the account manager with extra graphics."""
        print('Entering CLI...')
        prompt = '\n/> '
        while True:
            # Header part
            self._Header()
            
            # Main content
            self._Main()

            # Footer
            self._Footer()

            # Command input
            usr_inp = input(prompt)
            if usr_inp in AccountManager.q_cmds:
                print('Quiting...')
                quit()

            elif usr_inp in self.commands:
                self._commands(usr_inp)

            elif usr_inp in self.user_commands:
                self._logged_commands(usr_inp)
                
            else:
                print('Error! Command not recognised.'
                '\nTry "help" for more info.')
            
            print()

    def _commands(self, usr_inp):
        """Check if user input is in the <general commands>."""
        if usr_inp == 'help':
            self.Help()
        elif usr_inp == 'details':
            self.PrintDetails()
        elif usr_inp == 'register':
            self.CreateAccount()
        elif usr_inp == 'login':
            self.LogInAccount()

    def _logged_commands(self, usr_inp):
        """Check if user input is in the <logged in user commands>."""
        if self._is_logged():
            if usr_inp == 'logout':
                self.Logout()
        else:
            print('You are not logged in!')

    def _Header(self):
        """Header line for the CLI."""
        txt_line = 'Account Manager\t'
        if self._is_logged():
            txt_line += f'\tHello, {self.logged_acc.username}!'
        else:
            txt_line += 'Login/Create Acc'
        print(txt_line)
    
    def _Main(self):
        """Main content for the CLI."""
        print(f'|\t\tDetails\t\t|')
        if self._is_logged():
            #print(f'|\tUsername - {self.logged_acc.username}\t\t|')
            print(f'|\t{self.logged_acc.email}\t|')
        print(f'|\t\t-------\t\t|')

    @staticmethod
    def _Footer():
        """Footer part of the CLI, includes the command promt."""
        print('\tcopyright VM 2020')

    def Help(self):
        """Help Function to print info about each command."""
        print('List of general commands: ')
        for cmd in self.commands:
            print('\t-', cmd)
        print('List of user commands:')
        for cmd in self.user_commands:
            print('\t-', cmd)

    def PrintDetails(self):
        """Print details about the current state of the Account Manager."""
        print('Totals accounts: ', len(self.accounts))

        if self._is_logged():
            acc = self._get_acc_info()
            print('Username: ', acc.username)
            print('Password: ', acc.password)
            print('Email: ', acc.email)

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

        # Create the account, for databases
        new_acc = Account(username, password, email)

        # Add the account to the acc dict
        self.accounts[len(self.accounts)] = {
            'username': username,
            'password': password,
            'email': email,
        }

        # Store the account in json file
        with open(self.acc_filepath, 'w') as f:
            json.dump(self.accounts, f, indent=4)

        # Login automatically
        self._LogIn(username, password, email)

    def LogInAccount(self):
        """Log in to an existing account."""
        print('Login Form -')
        usr = input('Username: ')
        for acc in self.accounts:
            
            if usr == self.accounts[acc]['username']:
                pswd = input('Password: ')
                if pswd == self.accounts[acc]['password']:
                    print('Succesful Login!')
                    self._LogIn(usr, pswd, self.accounts[acc]['email'])

    def _LogIn(self, usr, pswd, email):
        """Login specific profile."""
        logged = Account(usr, pswd, email)
        self.logged_acc = logged
    
    def Logout(self):
        """Logout of the current account."""
        # Simple for now, will be extended
        if self._is_logged():
            print('Successful logout!')
            self.logged_acc = None
        else:
            print('You are not logged in!')

    def _is_logged(self):
        """Check if user is logged."""
        if self.logged_acc:
            return True

    # idk what i'm doing here
    def _get_acc_info(self):
        """Get the details of an account as a dict."""
        if self._is_logged():
            # return the logged account
            acc = self.logged_acc
        else:
            # return all of the accounts
            acc = [a for a in self.accounts]
        return acc
