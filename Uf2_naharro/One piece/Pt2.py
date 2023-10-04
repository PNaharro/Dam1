def funcion(entrada,inicio,L0,L1):
    if entrada == 0:
        return L0
    elif entrada == 1:
        return L1
    if inicio == entrada:
        return L0 + L1 - L0
    L2 = L0 + L1
    L0 = L1
    L1 = L2
    return funcion(entrada,inicio + 1,L0,L1)
print(funcion(4,1,2,1))