class Category:
    def __init__(self, name):
        self.category = name
        self.ledger = []
        self.amount = 0
        self.total = 0
        self.spent = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.amount += amount
        self.total += amount

    def withdraw(self, amount, description=""):
        if amount < self.amount:
            self.ledger.append({"amount": -amount, "description": description})
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
        string = self.category.center(30, "*") + "\n"
        
        for item in self.ledger:
            description_line = "{}:<23]}".format(item["description"])
            amount_line = "{:.2f}".format(item["amount"])

            string += f"{description_line[:23]}\n{amount_line}\n" 
        string += f"Total: {self.amount:.2f}"

        return string

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
    
    return string[:-2]


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
