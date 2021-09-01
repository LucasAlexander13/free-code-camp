from _typeshed import Self
class Category:
    def __init__(self, name):
        self.category = name
        self.ledger = []
        self.amount = 0

    def deposit(self, amount, description=""):
        text = f"\"amount\": {amount}, \"description\": {description}"
        self.ledger.append("{"+text+"}")
        self.amount += amount

    def withdraw(self, amount, description=""):
        if amount < self.amount:
            text = f"\"amount\": -{amount}, \"description\": {description}"
            self.ledger.append("{"+text+"}")
            self.amount -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.amount
    
    def transfer(self, amount, budget):
        if amount < self.amount:
            self.withdraw(amount, f"Transfer to {budget.category}")
            budget.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.amount:
            return False
        else:
            return True

def create_spend_chart(categories):