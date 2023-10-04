def funcion(num,cont):
    resultado = ''
    aux = ''
    if cont == num:
        return resultado
    else:
        aux = aux + str(cont)
        resultado = str(cont)+'\n'+funcion(num,cont+1)
        return resultado
print(funcion(9,1))
