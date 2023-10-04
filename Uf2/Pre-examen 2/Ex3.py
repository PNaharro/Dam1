def funcion(entrada,L0,L1):
    if entrada == 0:
        return 2
    elif entrada == 1:
        return 1
    if entrada == 0:
        return L1
    L2 = L0 + L1
    L0 = L1
    L1 = L2
    return funcion(entrada - 1,L0,L1)
print(funcion(1,2,1))