from re import I
from budget_class import Budget

def writeB():
    with open("budget.txt", "w") as budget:
        budget.write(input("Please enter a budget amount: "))

def writeN(TotalBudget):
    with open("budget.txt", "w") as budget:
        budget.write(str(TotalBudget.balance))

def readB():
    with open("budget.txt", "r") as budget:
        amount = float(budget.read())
        return amount