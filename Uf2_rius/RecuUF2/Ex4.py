def funcion(n,m):
    if n == 0:
        return 0
    if m ** 2 % 2 == 1:
        print(m ** 2,end=" ")
        return funcion(n - 1, m + 1)
    return funcion(n, m + 1)
funcion(4,1)