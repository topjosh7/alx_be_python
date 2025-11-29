class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with a starting balance (default 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to the balance. Do not print anything."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw amount if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in the exact grader format."""
        print(f"Balance: ${int(self.account_balance)}")

