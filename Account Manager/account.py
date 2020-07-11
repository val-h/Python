class Account:
    """A class to represent an account."""

    def __init__(self, username, password, email, /):
        """Create the account."""
        self.username = username
        self.password = password
        self.email = email
