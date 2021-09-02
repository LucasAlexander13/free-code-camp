class Category:
    def __init__(self, name):
        self.category = name
        self.ledger = []
        self.amount = 0
        self.total = 0
        self.spent = 0

    def deposit(self, amount, description=""):
        text = f"\"amount\": {amount}, \"description\": {description}"
        self.ledger.append("{"+text+"}")
        self.amount += amount
        self.total += amount

    def withdraw(self, amount, description=""):
        if amount < self.amount:
            text = f"\"amount\": -{amount}, \"description\": {description}"
            self.ledger.append("{"+text+"}")
            self.amount -= amount
            self.spent += amount
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

    def __str__(self):
        length = (30 - len(self.category)) / 2
        string = "*" * length + self.category + "*" * length + "\n"
        for dict in self.ledger:
            for key, value in dict.items():
                if key == "amount":
                    temp_string = str(value) + "\n"
                elif key == "description":
                    string += str(value) + "\n"
                    string += temp_string
        string += f"Total: {self.amount}"


def create_spend_chart(categories):
    string = "Percentage spent by category\n"
    dict_category = {}
    max_length = 0
    for item in categories:
        dict_category[item.category] = int(item.spent / item.total * 10)
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
            if dict_category[item.category] * 10 == table:
                string += "o  "
            else:
                string += "   "
        string += "\n"

    string += "    -" + "---" * len(categories) + "\n"

    for i in range(max_length):
        string += "     "
        for item in categories:
            if len(item.category) >= i:
                name = item.category
                string += name[i] + "  "
            else:
                string += "   "
        string += "\n"

