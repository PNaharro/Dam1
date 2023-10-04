lista = [10, 25, 31, 46, 52, 63, 71, 84, 91, 92]
while True:
    x = input("Dime el numero que buscas: ")
    if not x.isdigit():
        print("Introduce un valor valido")
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