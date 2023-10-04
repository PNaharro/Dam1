def burbuja_mas_menos(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] < lista[j + 1]:
                numero = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero
    return lista
def burbuja_menos_mas(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                numero = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero
    return lista
def funcion1(frase):
    resultado = ''
    if frase[len(frase)-1] == 'b':
        return frase
    else:
        resultado = funcion1(frase[:len(frase)-1])
        return resultado

def funcion(frase):
    vocales = 'aeiou'
    resultado = 0
    if len(frase) != 0:
       if frase[0].lower() in vocales:
           resultado = 1 +funcion(frase[1:])
       else:
         resultado = funcion(frase[1:])
    return resultado


def funcion3(frase):
    vocales = 'aeiou'
    resultado = ''
    if len(frase) != 0:
       if frase[0].lower() in vocales:
           resultado = frase[0].lower() + funcion3(frase[1:])
       else:
           resultado = frase[0].upper() + funcion3(frase[1:])
    return resultado




def funcion4(lista):
    resultado = []
    if len(lista) == 0:
        return resultado
    else:
        if lista[0]%2 == 0:
            resultado.append(int(lista[0]))
        return resultado+ funcion4(lista[1:])
print(funcion4([3,2,4]))