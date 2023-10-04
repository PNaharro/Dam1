archivo1 = open("archivo1.txt")
archivo2 = open("archivo2.txt")

lista = archivo1.read().split("\n")
print(lista)
for linia in archivo2:
    if int(linia) <= len(lista)-1:
        print(lista[int(linia)-1])
    else:
        print(linia,"no existente")

# lista = archivo1.readlines()
# print(lista)
# for linia in archivo2:
#     if int(linia) <= len(lista)-1:
#         print(lista[int(linia)-1].replace("\n",""))
#     else:
#         print(linia,"no existente")