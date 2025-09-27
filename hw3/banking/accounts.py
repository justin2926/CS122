from .exceptions import InvalidAmountError, InsufficientFundsError

class BankAccount():
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner_name = owner_name
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError("Amount cannot be negative!")
        self.initial_balance += amount

    def withdraw(self, amount):
        raise NotImplementedError("Method not implemented")

    def __str__(self):
        return f"Account owner: {self.owner_name}\nBalance: {self.initial_balance:.2f}"

class SavingAccount(BankAccount):
    withdrawal_fee = 2.00

class CheckingAccount(BankAccount):
    withdrawwal_fee = 1.00