def funcion (dividendo,divisor):
    resultado = 0
    if dividendo < divisor:
        return resultado
    else:
        resultado = 1 + funcion(dividendo-divisor,divisor)
        return resultado
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
print(funcion(dividendo,divisor))