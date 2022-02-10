class Budget():
    def __init__(self, balance):
        self.balance = balance      

    
    
    def __repr__(self):
        return f"Your current balance is {self.balance}"

    def deposit(self,amount):
        self.amount = amount
        self.balance += self.amount
        return amount



    def withdraw(self,amount):
        self.amount = amount
        self.balance -= self.amount
        return amount