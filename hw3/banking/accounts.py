class BankAccount():
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner_name = owner_name
        self.initial_balance = initial_balance

    def deposit(self, amount):
        return 0

    def withdraw(self, amount):
        return 0

    def __str__(self):
        return 0

class SavingAccount(BankAccount):
    withdrawal_fee = 2.00

class CheckingAccount(BankAccount):
    withdrawwal_fee = 1.00