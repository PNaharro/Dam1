def funcion(frase):
    resultado = ''
    if len(resultado) == 0:
        return resultado
    else:
        if frase[len(frase)] == ' ':
            print(resultado)
        resultado= frase[len(frase)] + funcion(frase[:len(frase)-1])
        return resultado
print(funcion('hola buenas'))