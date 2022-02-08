'''
Create a new Python file and write a program that does the following:

Asks for an input from the user as a mark.
If the mark is greater that 85 print "Distinction"
If the mark is between 65 and 85 print "Pass"
Anything else print "Fail"
Try to do this both with and without elif statements.
'''

# mark = int(input("Please enter your score: "))
# if mark > 85:
#     print("Distinction")
# elif mark >= 65:
#     print("Pass")
# else:
#     print("Fail")

# mark = int(input("Please enter your mark: "))
# if mark > 85:
#     print("Distinction")
# if 85 >= mark >= 65:
#     print("Pass")
# if mark < 65:
#     print("Fail")

# score = int(input("Enter your exam score "))
# key = 0
# if score > 85 : key = 1
# if 85 >= score >= 65: key = 2
# if score < 65 : key = 3
# Exam_Score = {
#                 1: "Distinction",
#                 2: "Pass",
#                 3: "Fail"
#              }
# print(Exam_Score.get(key))

score = int(input("Enter your exam score "))
key = []
if score > 85 : key = 0
if 85 >= score >= 65 : key = 1
if score < 65 : key = 2
Exam_Score = ["Distinction", "Pass", "Fail"]
print(Exam_Score[key])