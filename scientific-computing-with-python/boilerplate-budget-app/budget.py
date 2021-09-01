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




def create_spend_chart(categories):