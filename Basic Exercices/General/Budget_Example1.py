from myclasses import Budget

working = True
listofcurrentbudgets = []


while working:
    print("Menu: 1. Instantiate Budgets * 2. View Budgets * 3. Edit Budgets")
    control = int(input("Enter the number of the menu option you wish to use: "))

    if control == 1:
        food = Budget(100, "food")
        listofcurrentbudgets.append(food)
        bills = Budget(30, "bills")
        listofcurrentbudgets.append(bills)
        
    elif control == 2:
        control2 = True
        while control2:
            print(f"You have {str(len(listofcurrentbudgets))} current budgets.")
            numberedbudgets = 1
            for item in listofcurrentbudgets:
                print(f"{numberedbudgets}: {item.name}")
                numberedbudgets += 1
            userchoice1 = int(input("Which of these budgets do you want to choose? "))
            if userchoice1 == 1:
                print(f"Food: {listofcurrentbudgets[0]}")
                control2 = True
            else:
                print(f"Bills: {listofcurrentbudgets[1]}")
                control2 = False
    elif control == 9:
        working = False