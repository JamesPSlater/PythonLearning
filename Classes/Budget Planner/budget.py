'''
create class - Budget
name each object after the budget it's for
withdraw method
deposit method
debugging code
'''




class Budget():
    def __init__(self, balance):
        self.balance = float(balance)       

    
    
    def __repr__(self):
        return f"Your current balance is {self.balance}"

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount


    def withdraw(self,amount):
        self.amount = amount
        self.balance = self.balance - self.amount


TotalBudget = Budget(500)

Budget.deposit(TotalBudget, 200)
print(f"{TotalBudget} after deposit of ?????")
Budget.withdraw(TotalBudget, 500)
print(f"{TotalBudget} after withdrawal of ?????")
