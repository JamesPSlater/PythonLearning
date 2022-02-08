# def greet(fname, words):
#     return f"{words} {fname}"

# name = input("Please enter your name: ")
# greeting = input("Greeting: ")
# print(greet(name, greeting))


def grading(hScore, aScore, eScore):
    percentage = (hScore + aScore + eScore) / 175 * 100
    return percentage    


name = input("Please enter a name: ")
hScore = int(input("Please enter their homework score: "))
while hScore > 25:
    print("Please enter a max number of 25")
    hScore = int(input("Please enter their homework score: "))


aScore = int(input("Please enter their asessment score: "))
while aScore > 50:
    print("Please enter a max number of 50")
    aScore = int(input("Please enter their asessment score: "))

eScore = int(input("Please enter their eScore score: "))
while eScore > 100:
    print("Please enter a max number of 100")
    eScore = int(input("Please enter their asessment score: "))

result = grading(hScore, aScore, eScore)

if result >= 80:
    grade = "A"
elif result >= 70:
    grade = "B"
elif result >= 60:
    grade = "C"
else:
    grade = "F"

print(f"{name} scored {result}% with a grade of {grade}")