def funcion(num):
    resultado = ''
    if num == 0:
        return resultado
    else:
        resultado = str(num%10) + funcion(num//10)
        return resultado
print(funcion(123))