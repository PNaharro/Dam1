def funcion(lista):
    resultado = 1
    if len(lista) == 0:
        return resultado
    else:
        resultado = lista[0] * funcion(lista[1:])
        return resultado
lista = [3,6]
print(funcion(lista))