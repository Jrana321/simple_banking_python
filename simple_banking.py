class Bank:
    def __init__(self, account_holder, initial_balance):
        self.account_holder_name = account_holder
        self.initial_balance = initial_balance
        self.transaction_history = []

    def deposit_amount(self, amount):
        if amount > 0:
            self.initial_balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print(f"{self.account_holder_name}, your account has been deposited {amount} successfully.")
        else:
            print("Sorry! Insufficient amount to deposit.")

    def withdraw_amount(self, amount):
        if amount > 0 and amount <= self.initial_balance:
            self.initial_balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Amount {amount} withdrawn successfully!")
        else:
            print("Sorry! Insufficient amount for withdrawal.")

    def get_balance(self):
        print(f"Your account balance is {self.initial_balance}")

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

# Create a bank account object
obj = Bank("XYZ", 1000)

# Perform transactions
obj.deposit_amount(500)
obj.get_balance()
obj.withdraw_amount(400)
obj.get_balance()
obj.view_transaction_history()
