lista1 = []
lista2 = []
x = int(input("Cuantas palabras quieres introducir en la lista1: "))
for i in range(x):
    palabra1 = input("Palabra: ")
    lista1.append(palabra1)
y = int(input("Cuantas palabras quieres introducir en la lista2: "))
for i in range(y):
    palabra2 = input("Palabra: ")
    lista2.append(palabra2)

for i in lista1:
    for j in lista2:
        if i == j:
            print("Las palabras que se repiten son:",i)
            break
tupla1 = []
for i in lista1:
    for j in lista2:
        if i != j:
            tupla1.append(i)

print(tupla1)



input()
print(lista1)
print(lista2)