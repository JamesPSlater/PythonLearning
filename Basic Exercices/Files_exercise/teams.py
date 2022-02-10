with open("teams.txt", "w") as file:
    for line in range(1,6):
        newline = "Team" + str(line) + "\n"
        file.write(newline)


with open("teams.txt", "r") as file:
    content = file.readlines()


for team in content:
    if content.index(team) == 0 or content.index(team) == 3:
        print(team)




with open("teams.txt", "r") as file:
    content = file.readlines()
    
    
with open("teams.txt", "w") as file:
    for team in content:
        if content.index(team) == 0:
            file.write("This is a new line \n")
        else:
            file.write(team)

