'''
Way to add more budget types:

'''

from os import path
import budget_func as bf
from budget_class import Budget

if not path.isfile("./budget.txt"):
    bf.writeB()

Active = True
tBudget = Budget(bf.readB())
while Active == True:

    choice = int(input("1. Deposit - 2. Withdraw - 3.View balance - 4.Exit      "))


    if choice == 1:
        dValue = float(input("How much would you like to deposit?     "))
        Budget.deposit(tBudget, dValue)
        bf.writeN(tBudget)
        print(f"{tBudget} after deposit of {dValue}")

    elif choice == 2:
        wValue =  float(input("How much would you like to withdraw?    "))
        Budget.withdraw(tBudget, wValue)
        bf.writeN(tBudget)
        print(f"{tBudget} after withdrawal of {wValue}")

    elif choice == 3:
        print(tBudget)
    
    elif choice == 4:
        Active = False
    
    else:
        print("Please enter a valid choice:")
        choice = int(input("1. Deposit - 2. Withdraw - 3.View balance - 4.Exit      "))