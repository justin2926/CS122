from .exceptions import InvalidAmountError, InsufficientFundsError

class BankAccount():
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner_name = owner_name
        self.initial_balance = initial_balance
        self.current_balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError("Amount cannot be negative!")
        self.current_balance += amount

    def withdraw(self, amount):
        raise NotImplementedError("Method not implemented")

    def __str__(self):
        return f"Account owner: {self.owner_name}\nBalance: {self.current_balance:.2f}"

class SavingAccount(BankAccount):
    def __init__(self, owner_name, initial_balance=0.0, savings_balance=0.0):
        super().__init__(owner_name, initial_balance)
        self.savings_balance = savings_balance
        self.withdrawal_fee = 2.00

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmountError("Amount cannot be negative!")
        elif amount + self.withdrawal_fee > self.current_balance:
            raise InsufficientFundsError("Amount requested and fee is greater than the current balance!")
        else:
            self.current_balance = self.current_balance - (self.withdrawal_fee + amount)

class CheckingAccount(BankAccount):
    withdrawwal_fee = 1.00