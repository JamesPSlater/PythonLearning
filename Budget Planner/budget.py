'''
Way to add more budget types:

'''

from os import path
import budget_func as bF
from budget_class import Budget as bC

if not path.isfile("./budget.txt"):
    bF.writeB()

Active = True
tBalance = bC(bF.readB())
while Active == True:

    choice = int(input("1. Deposit - 2. Withdraw - 3.View balance - 4.Exit      "))


    if choice == 1:
        dValue = float(input("How much would you like to deposit?     "))
        bC.deposit(tBalance, dValue)
        bF.writeN(tBalance)
        print(f"{tBalance} after deposit of {dValue}")

    elif choice == 2:
        wValue =  float(input("How much would you like to withdraw?    "))
        bC.withdraw(tBalance, wValue)
        bF.writeN(tBalance)
        print(f"{tBalance} after withdrawal of {wValue}")

    elif choice == 3:
        print(tBalance)
    
    elif choice == 4:
        Active = False
    
    else:
        print("Please enter a valid choice:")
        choice = int(input("1. Deposit - 2. Withdraw - 3.View balance - 4.Exit      "))