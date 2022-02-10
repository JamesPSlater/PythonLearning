from budget_class import Budget

def main():
    TotalBudget = Budget(float(input("Please enter a starting budget amount: ")))
    Active = True

    while Active == True:

        choice = int(input("1. Deposit - 2. Withdraw - 3.View balance - 4.Exit      "))


        if choice == 1:
            depAmount = float(input("How much would you like to deposit?     "))
            Budget.deposit(TotalBudget, depAmount)
            print(f"{TotalBudget} after deposit of {depAmount}")

        elif choice == 2:
            withAmount =  float(input("How much would you like to withdraw?    "))
            Budget.withdraw(TotalBudget, withAmount)
            print(f"{TotalBudget} after withdrawal of {withAmount}")

        elif choice == 3:
            print(TotalBudget)
        
        elif choice == 4:
            Active = False
        
        else:
            print("Please enter a valid choice:")
            choice = int(input("1. Deposit - 2. Withdraw - 3.View balance - 4.Exit      "))