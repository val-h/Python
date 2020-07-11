class Account:
    """A class to represent an account."""

    def __init__(self, username, password, email, /):
        """Create the account."""
        self.username = username
        self.password = password
        self.email = email
        
        self.acc_type = 'acc'

class User(Account):
    """User account with basic functionality."""

    def __init__(self, username, password, email, /):
        super.__init__()

        self.acc_type = 'user'

class Admin(Account):
    """Admin account with extra privilages."""
    
    def __init__(self, username, password, email, /):
        super.__init__()

        self.acc_type = 'admin'
        