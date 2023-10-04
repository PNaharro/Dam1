import random
lista = []
for x in range(random.randint(5,10)):
    lista.append(random.randint(0,30))
print(lista)
for i in range(len(lista)-1):
    for j in range(len(lista)-i-1):
        if lista[j] < lista[j+1]:
            numero = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = numero
print(lista)