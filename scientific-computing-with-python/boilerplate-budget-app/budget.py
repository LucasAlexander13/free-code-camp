from _typeshed import Self
class Category:
    def __init__(self, name):
        self.category = name
        self.ledger = []

    def deposit(self, amount, description=""):
        text = f"\"amount\": {amount}, \"description\": {description}"
        self.ledger.append("{"+text+"}")





def create_spend_chart(categories):