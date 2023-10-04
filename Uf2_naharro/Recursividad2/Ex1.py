def funcion(n):
    resultado = 1
    if n == 0:
        resultado = 2
        return resultado
    else:
        resultado = resultado * ((2*n)/(2*n-1)) * ((2*n)/(2*n+1)) * funcion(n-1)
        return resultado

print(funcion(900))