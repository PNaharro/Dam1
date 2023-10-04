import random
lista = []
for x in range(random.randint(5,10)):
    lista.append(random.randint(0,30))
print(lista)
for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] > lista[j]:
            numero = lista[i]
            lista[i] = lista[j]
            lista[j] = numero
print(lista)
