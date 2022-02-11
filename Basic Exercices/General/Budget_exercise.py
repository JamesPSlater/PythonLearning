from Budget_exercise_class import Budget

food = Budget(100)
clothes = Budget (200)

print(food)

clothes.deposit(food.withdraw(45))


print(food)
print(clothes)