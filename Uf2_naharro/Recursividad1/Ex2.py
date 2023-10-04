def funcion(numero):
    suma = 0
    if numero < 1:
        return suma
    else:
        suma += numero % 10 + funcion(numero // 10)
        return suma
numero = int(input("Numero: "))
print(funcion(numero))