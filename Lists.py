list1 = [12, "Hello", 56.44, False, 43, "World", False, 32, False, 7, "Hello", "Hello", "Hello"] #Creating a list

list1.insert(13, True) #inserting into list
print(list1)

def test(): #Function
    if True in list1:
        print(f"{list1[1]} {list1[5]}")
    else:
        print("This is not right")
test()

# print(set(list1)) #prints unique information


# dict1 = {1:"Slot1", 2:"Slot2", 3:"Slot3"} #Making a dictionary
# dict1[4] = "Slot 4" #Adding to a dictionary
# print(dict1)
# print(dict1.keys())

# tup1 = ("item1", "item2", "item3") #tuple, cant be changed
# print(tup1)