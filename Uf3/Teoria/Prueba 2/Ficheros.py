arch1 = open("persones.txt", "r")
arch2 = open("archivo2", "r")

for i in arch2:
    print(str(i).replace("\n",""))
print(arch1.read())