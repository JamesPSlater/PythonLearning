# def greet(fname, words):
#     return f"{words} {fname}"

# name = input("Please enter your name: ")
# greeting = input("Greeting: ")
# print(greet(name, greeting))


def grading(hwscore, ascore, exam):
    percentage = (hwscore + ascore + exam) / 175 * 100
    return percentage   


name = input("Please enter a name: ")
hwscore = int(input("Please enter their homework score: "))
while hwscore > 25:
    print("Please enter a max number of 25")
    hwscore = int(input("Please enter their homework score: "))


ascore = int(input("Please enter their asessment score: "))
while ascore > 50:
    print("Please enter a max number of 50")
    ascore = int(input("Please enter their asessment score: "))

exam = int(input("Please enter their exam score: "))
while exam > 100:
    print("Please enter a max number of 100")
    exam = int(input("Please enter their asessment score: "))

result = grading(hwscore, ascore, exam)

if result >= 80:
    grade = "A"
elif result >= 70:
    grade = "B"
elif result >= 60:
    grade = "C"
else:
    grade = "F"

print(f"{name} scored {result}% with a grade of {grade}")