'''
create class - Budget
name each object after the budget it's for
withdraw method
deposit method
debugging code
'''




class Budget():
    def __init__(self, balance):
        self.balance = balance      

    
    
    def __repr__(self):
        return f"Your current balance is {self.balance}"

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount


    def withdraw(self,amount):
        self.amount = amount
        self.balance = self.balance - self.amount


TotalBudget = Budget(float(input("Please enter a starting budget amount: ")))

Budget.deposit(TotalBudget, float(input("How much would you like to deposit?")))
print(f"{TotalBudget} after deposit of ?????")

Budget.withdraw(TotalBudget, float(input("How much would you like to withdraw?")))
print(f"{TotalBudget} after withdrawal of ?????")
