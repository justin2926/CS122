from .exceptions import InvalidAmountError, InsufficientFundsError

class BankAccount():
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner_name = owner_name
        self.initial_balance = initial_balance
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount cannot be negative or zero!")
        self.balance += amount

    def withdraw(self, amount):
        raise NotImplementedError("Method not implemented")

    def __str__(self):
        return f"Account Owner: {self.owner_name}, Balance: ${self.balance:.2f}"

class SavingAccount(BankAccount):
    def __init__(self, owner_name, initial_balance=0.0):
        super().__init__(owner_name, initial_balance)
        self.withdrawal_fee = 2.00

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmountError("Amount cannot be negative!")
        
        if self.balance < (amount + self.withdrawal_fee):
            raise InsufficientFundsError("Amount requested and fee is greater than the current balance!")

        self.balance = self.balance - (self.withdrawal_fee + amount)

class CheckingAccount(BankAccount):
    def __init__(self, owner_name, initial_balance=0.0):
        super().__init__(owner_name, initial_balance)
        self.withdrawal_fee = 1.00

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmountError("Amount cannot be negative!")
        
        if self.balance < (amount + self.withdrawal_fee):
            raise InsufficientFundsError("Amount requested and fee is greater than the current balance!")

        self.balance = self.balance - (self.withdrawal_fee + amount)