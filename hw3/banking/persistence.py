class Bank:
    def __init__(self, db_path):
        self.accounts = {}

    def create_account(self, account_type, owner_name, initial_balance=0.0):
        self.account_type = account_type
        self.owner_name = owner_name
        self.initial_balance = initial_balance
    
    def get_account(self, owner_name):
        return 0
    
    def save_data(self):
        return 0
    
    def load_data(self):
        return 0