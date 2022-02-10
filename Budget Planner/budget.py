'''
Way to add more budget types:

'''

from os import path
import budget_func as bf
from budget_class import Budget

if not path.isfile("./budget.txt"):
    bf.writeB()

Active = True
TotalBudget = Budget(bf.readB())
while Active == True:

    choice = int(input("1. Deposit - 2. Withdraw - 3.View balance - 4.Exit      "))


    if choice == 1:
        depAmount = float(input("How much would you like to deposit?     "))
        Budget.deposit(TotalBudget, depAmount)
        bf.writeN(TotalBudget)
        print(f"{TotalBudget} after deposit of {depAmount}")

    elif choice == 2:
        withAmount =  float(input("How much would you like to withdraw?    "))
        Budget.withdraw(TotalBudget, withAmount)
        bf.writeN(TotalBudget)
        print(f"{TotalBudget} after withdrawal of {withAmount}")

    elif choice == 3:
        print(TotalBudget)
    
    elif choice == 4:
        Active = False
    
    else:
        print("Please enter a valid choice:")
        choice = int(input("1. Deposit - 2. Withdraw - 3.View balance - 4.Exit      "))