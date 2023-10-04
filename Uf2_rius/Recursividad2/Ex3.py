def funcion(a,b):
    resultado = 0
    if a < 1:
        return resultado
    else:
        if a%2 != 0:
            resultado = b + funcion(a//2,b*2)
        else:
            resultado = funcion(a // 2, b * 2)
        return resultado
print(funcion(27,82))