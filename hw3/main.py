from banking.accounts import BankAccount, SavingAccount, CheckingAccount
from banking.exceptions import InsufficientFundsError, InvalidAmountError
from banking.persistence import *

justin = BankAccount("Justin Nguyen")

justin.deposit(290)
print(justin)
