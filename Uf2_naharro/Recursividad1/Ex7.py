def funcion(n):
    suma = 0
    if n == 1:
        return suma
    else:
        if n%2==0:
            suma = n + funcion(n-1)
            return suma
        else:
            return funcion(n-1)
# n = int(input("Numero: "))
# print(funcion(n))

#Profe
def numerosPares(n):
    if n == 2:
        resultado = 2
        return resultado
    if n%2 != 0:
        resultado = numerosPares(n-1)
        return resultado
    else:
        resultado = n + numerosPares(n-2)
        return resultado
print(numerosPares(11))