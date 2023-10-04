import random
lista = []
for x in range(9):
    lista.append(random.randint(100,500))
for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] > lista[j]:
            numero = lista[i]
            lista[i] = lista[j]
            lista[j] = numero
while True:
    x = input("Dime el numero que buscas: ")
    if not x.isdigit():
        print("Introduce un valor valido")
    elif int(x) < 100 or int(x) > 500:
        print("Pon un numero entre 100 y 500 porque el que me dices no esta")
    else:
        x = int(x)
        break
sup = len(lista)-1
inf = 0
while sup >= inf:
    medio = (sup + inf)//2
    if x == lista[medio]:
        print("Esta el numero")
        break
    elif x < lista[medio]:
        sup = medio-1
    elif x > lista[medio]:
        inf = medio+1
    if inf > sup:
        print("El numero no esta")
print(lista)