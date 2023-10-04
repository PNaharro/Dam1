#Pau
def funcion(posicion):
    lista = [20,10,5,2,3]
    suma = 0
    if posicion == len(lista):
        return suma
    else:
        suma = lista[posicion] + funcion(posicion + 1)
        return suma
#print(funcion(0))

#Profe
def sumaNumLista(lista):
    resultado = 0
    if len(lista) == 0:
        return resultado
    else:
        resultado = lista[0] + sumaNumLista(lista[1:])
        return  resultado
lista = [3,6,8,2]
#print(sumaNumLista(lista))