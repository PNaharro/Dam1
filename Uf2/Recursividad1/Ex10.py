def funcion(v1):
    resultado = False
    if len(v1) == 0:
        return resultado
    if len(v1)-1 == v1[len(v1)-1]:
        resultado = True
        return resultado
    else:
        resultado = funcion(v1[:len(v1)-1])
        return resultado
print(funcion([1,2,3,4]))

#Profe
def compruebaIndices(v1):
    resultado = False
    if len(v1) == 0:
        return resultado
    elif v1[-1] == len(v1)-1:
        resultado = True
        return resultado
    else:
        resultado = compruebaIndices(v1[:-1])
        return resultado
print(compruebaIndices([0,2,3]))