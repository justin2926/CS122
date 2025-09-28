import shelve
from banking.accounts import BankAccount, SavingAccount, CheckingAccount

class Bank:
    def __init__(self, db_path):
        self.accounts = {}
        self.db_path = db_path

    def create_account(self, account_type, owner_name, initial_balance=0.0):
        if owner_name in self.accounts:
            print(f"{owner_name} already exists!")
            return False
        else:
            if account_type == "saving":
                self.accounts[owner_name] = SavingAccount(owner_name, initial_balance)
            elif account_type == "checking":
                self.accounts[owner_name] = CheckingAccount(owner_name, initial_balance)
            return True

    def get_account(self, owner_name):
        if owner_name not in self.accounts:
            return None
        return self.accounts[owner_name]
    
    def save_data(self):
        with shelve.open(self.db_path) as db:
            db.update(self.accounts)
    
    def load_data(self):
        try:
            with shelve.open(self.db_path) as db:
                for key in db:
                    self.accounts[key] = db.get(key)
        except FileNotFoundError:
            self.accounts = {}