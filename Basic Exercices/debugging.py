# Burger = 10
# user_funds = 10.31
# item_price = Burger


# if item_price < user_funds:
#     print("You have enough money!")
# elif item_price == user_funds:
#     print("You have the precise amount of money")
# elif item_price < user_funds:
#     print("Sorry you don't have enough money")

# def product(n):
#     total = 1
#     for n in n:
#         total *= n
#     return total

# print(product([4,4,5]))




# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return True
#             else:            
#                 return False

# print(is_prime(3))

import pdb

# pdb.set_trace()
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(item_list.index[i])

print(item_list[5])