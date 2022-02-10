class Student():
    def __init__(self, name, age, class_ = "Student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def __repr__(self):
        return f"{self.name} is {self.age} years old, and is in class {self.class_}"

    def aScore(self, score1, score2, score3): 
        result = (score1 + score2 + score3) / 3
        self.avgScore = int(result)
        return result


stud1 = Student("James", "29", "English")
stud1.aScore(88, 33, 55)

stud2 = Student("Alex", "18", "German")

stud3 = Student("Pan", "31", "French")

print(stud1)
print(stud1.avgScore)