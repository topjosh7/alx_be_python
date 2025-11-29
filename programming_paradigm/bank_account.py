class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited ${int(amount)}")
        print(f"Balance: ${int(self.account_balance)}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew ${int(amount)}")
            print(f"Balance: ${int(self.account_balance)}")
            return True
        else:
            print("Insufficient funds")
            print(f"Balance: ${int(self.account_balance)}")
            return False

    def display_balance(self):
        print(f"Balance: ${int(self.account_balance)}")
