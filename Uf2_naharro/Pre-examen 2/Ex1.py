def funcion(base, altura, alturaI):
    x = "*" * base
    if alturaI == altura:
        return x
    print(x)
    return funcion(base,altura,alturaI + 1)
print(funcion(4,5,1))