def funcion(x,n):
    potencia = 1
    if n == 0:
        return potencia
    else:
        potencia = x * funcion(x,n-1)
        return potencia
x = int(input("Numero: "))
n = int(input("Potencia: "))
print(funcion(x,n))