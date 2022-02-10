with open("teams.txt", "w") as file:
    for line in range(1,6):
        newline = "Team" + str(line) + "\n"
        file.write(newline)

with open("teams.txt", "r") as file:
    content = file.readlines()
    print(content[0])
    print(content[3])