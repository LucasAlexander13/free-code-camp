class Category:
    def __init__(self, name):
        self.category = name
        self.ledger = []
        self.balance = 0
        self.total = 0
        self.spent = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        self.total += amount

    def withdraw(self, amount, description=""):
        if amount < self.balance:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            self.spent += amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, budget):
        if amount < self.balance:
            self.withdraw(amount, f"Transfer to {budget.category}")
            budget.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    def __str__(self):
        string = self.category.center(30, "*") + "\n"
        
        for item in self.ledger:
            description_line = "{:<23}".format(item["description"])
            amount_line = "{:>7.2f}".format(item["amount"])

            string += f"{description_line[:23]}{amount_line[:7]}\n" 
        string += f"Total: {self.balance:.2f}"

        return string

def create_spend_chart(categories):
    string = "Percentage spent by category\n"
    
    spent = {}
    max_length = 0
    for item in categories:
        spent[item.category] = int(item.spent / item.total * 10)

        if len(item.category) > max_length:
            max_length = len(item.category)
    
    for i in range(11):
        table = 100 - i * 10
        if table == 100:
            string += f"{table}| "
        elif table == 0:
            string += f"  {table}| "
        else:
            string += f" {table}| "

        for item in categories:
            if spent[item.category] * 10 >= table:
                string += "o  "
            else:
                string += "   "
        string += "\n"

    string += "    -" + "---" * len(categories) + "\n"

    for i in range(max_length):
        string += "     "
        for item in categories:
            if len(item.category) > i:
                name = item.category
                string += name[i] + "  "
            else:
                string += "   "
        string += "\n"
    
    return string[:-2]
