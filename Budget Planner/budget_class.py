class Budget():
    def __init__(self, tBalance):
        self.tBalance = tBalance      

    
    
    def __repr__(self):
        return f"Your current balance is {self.tBalance}"

    def deposit(self,dValue):
        self.dValue = dValue
        self.tBalance += self.dValue
        return dValue



    def withdraw(self,wValue):
        self.wValue = wValue
        self.tBalance -= self.wValue
        return wValue