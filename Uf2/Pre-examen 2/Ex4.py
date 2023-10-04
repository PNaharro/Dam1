def funcion(n,m):
    resultado = m * m
    if n == 0:
        return
    if resultado % 2 == 1:
        print(resultado)
        return funcion(n - 1,m+1)
    elif resultado % 2 == 0:
        return funcion(n, m +1)
funcion(498,10)