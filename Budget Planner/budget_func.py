from re import I
from budget_class import Budget

def writeB():
    with open("budget.txt", "w") as fBudget:
        fBudget.write(input("Please enter a budget amount: "))

def writeN(tBalance):
    with open("budget.txt", "w") as fBudget:
        fBudget.write(str(tBalance.balance))

def readB():
    with open("budget.txt", "r") as fBudget:
        tValue = float(fBudget.read())
        return tValue