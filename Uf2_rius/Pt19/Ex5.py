import random
lista = []
for x in range(random.randint(5,10)):
    lista.append(random.randint(0,30))
print(lista)
def procedimient(lista):
    for i in lista:
        print("*"*i)
procedimient(lista)