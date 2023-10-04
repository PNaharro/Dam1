def funcion(n,k):
    resultado = 0
    if k == 0:
        resultado = 1
        return resultado
    if n == 0:
        return resultado
    resultado = funcion(n-1,k-1)+funcion(n-1,k)
    return resultado

for n in range(10,20):
    for k in range(10,20):
        print("{} sobre {} = {}".format(n,k,funcion(n,k)))