def funcion(x,n):
    suma = 0
    if n == 0:
        return suma
    else:
        suma = x + funcion(x,n-1)
        return suma
x = int(input("Multiplicado: "))
n = int(input("Multiplicador: "))
print(funcion(x,n))