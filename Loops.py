# control = 0

# while control <= 10:
#     print(f"Control is: {control}")
#     control += 1 #same as 'control = control +1'




# running = True

# while running:
#     print("Menu - 1. print hello - 2. print goodbye - 0. exit")
#     input1 = int(input("Please choose an option: "))
#     if input1 == 1:
#         print("hello")
#     elif input1 == 2:
#         print("goodbye")
#     elif input1 == 0:
#         running = False
#     else:
#         print("Not a valid option! Try again.")
#     #Currently dies on not int values



# list1 = ["Tom", "Tim", "Tam"]
# str1 = "Hello World"
# dict1 = {1:"Tom", 2:"Tim", 3:"Tam"}
# list2 = range(1, 101)

# for num in list2:
#     if num == 1 or num == 2:
#         continue #or break
#     else:
#         print(num)



# control1 = 0
# control2 = 0

# while control1 < 10:
#     control1+=1
#     print("control1 = " + str(control1))
#     while control2 < 5:
#         control2 += 1
#         print("control2 = " + str(control2))



from multiprocessing.dummy import Namespace


count = 0
names = []

while count < 5:
    name = str(input("What is your name?"))
    names.append(name)
    count += 1


for name in names:
    print(name + "is awesome!")