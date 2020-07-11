import json

from account import Account

class AccountManager:
    """Acount Manager class with CRUD functionality."""

    q_cmds = {'quit', 'exit', 'terminate'}

    def __init__(self):
        """Initialize the account manager a load data from a json file."""
        # Dictionary to hold all the accounts and to load from
        with open('Account Manager\\accounts.json') as f:
            acc_dict = json.load(f)

        # Accounts dict
        self.accounts = acc_dict

        # Commands list
        self.commands = ['help', 'details', 'register', 'login', AccountManager.q_cmds]

        # Command Line Interface
        print('Entering CLI...')
        self.CommandLine()

    def CommandLine(self):
        """Command line for the account manager with extra graphics."""
        # Header part
        # refactoring required...
        header = self._Header()
        
        # Main content

        if header == True:
            # User is logged in
            pass
        else:
            print('\tYou are not logged in! Please create an account.')

        # Footer - Command input
        prompt = '\n/> '
        while True:
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
        txt_line += '\tLogin/Create Acc'
        print(txt_line)
        
        # Return true of false if the user is logged on.
        return False

    def Help(self):
        """Help Function to print info about each command."""
        print('List of commands: ')
        for item in self.commands:
            print('\t-', item)

    def PrintDetails(self):
        """Print details about the current state of the Account Manager."""
        print('Totals accounts: ', len(self.accounts))

        for acc in self.accounts:
            print(f"Username: {acc['username']}")
            print(f"Password: {acc['password']}")
            print(f"Email: {acc['email']}")

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
        pass
