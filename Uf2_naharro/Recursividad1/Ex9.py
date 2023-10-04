def comparaVectores(v1,v2):
    resultado = False
    if len(v1) != len(v2):
        return resultado
    if len(v1) == 0 and len(v2) == 0:
        resultado = True
        return resultado
    elif v1[0] != v2[0]:
        return resultado
    else:
        resultado = comparaVectores(v1[1:],v2[1:])
        return resultado
print(comparaVectores([1,2,3],[1,2,3]))