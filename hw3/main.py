from banking.accounts import BankAccount, SavingAccount, CheckingAccount
from banking.exceptions import InsufficientFundsError, InvalidAmountError
from banking.persistence import *

bank1 = Bank('bank1.shelf')
bank2 = Bank('bank2')

bank1.create_account("saving", "Justin", 500)
bank1.create_account("checking", "Timmy", 300)
bank1.create_account("checking", "Tony", 200)

print(bank1.get_account("Tony"))
print(bank1.accounts)

print(bank1.save_data())

bank = Bank('skjsdkjdskjd.db')
bank.load_data()
print(bank.accounts)















