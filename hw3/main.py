from banking.accounts import BankAccount, SavingAccount, CheckingAccount
from banking.exceptions import InsufficientFundsError, InvalidAmountError
from banking.persistence import *

justin = BankAccount("Justin Nguyen", 105.00)

justin.deposit(-50)
print(justin.current_balance)

