from re import I
from budget_class import Budget

def writeB():
    with open("budget.txt", "w") as budget:
        budget.write(input("Please enter a budget amount: "))

def writeN(tBudget):
    with open("budget.txt", "w") as budget:
        budget.write(str(tBudget.balance))

def readB():
    with open("budget.txt", "r") as budget:
        tValue = float(budget.read())
        return tValue