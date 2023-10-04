# personas = open("persones2.txt")
#
# for linia in personas:
#     if linia.find("Nombre") != -1:
#         print(linia.split("=")[1].replace(" ",""))

personas = open("persones.txt")

for i in personas:
        print(i.split("!")[0].split(":")[1])