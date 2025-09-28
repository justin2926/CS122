from banking.accounts import BankAccount, SavingAccount, CheckingAccount
from banking.exceptions import InsufficientFundsError, InvalidAmountError
from banking.persistence import *

justin = BankAccount("Justin Nguyen", 105.00)
print(justin)
justin.deposit(50)
# justin.withdraw(10)

justin_savings = SavingAccount("Justin's Savings", 200)
justin_savings.withdraw(10)
print(justin_savings)


