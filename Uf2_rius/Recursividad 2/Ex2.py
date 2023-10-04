def funcion(x):
    resultado = x
    if len(str(x)) == 1:
        return resultado
    resultado = funcion(x//10)
    print(str(x)[:3])
    return resultado

print(funcion(123))