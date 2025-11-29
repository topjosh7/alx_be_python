# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a BankAccount with an optional initial balance (default 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account.
        Assumes amount is a number (int/float)."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist.
        Returns True if withdrawal succeeded, False otherwise."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current balance: ${self.account_balance:.2f}")
