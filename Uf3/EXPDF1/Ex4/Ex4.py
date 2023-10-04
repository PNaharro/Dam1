personas = open("../Ex3/persones.txt")

for i in personas:
    if int(i.split("!")[3].split(":")[1]) >= 18:
        print(i.split("!")[0].split(":")[1])