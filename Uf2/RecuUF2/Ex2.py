def funcion(palabra):
    if len(palabra) == 1:
        return True
    elif palabra[0].lower() > palabra[1].lower():
        return False
    return funcion(palabra[1:])
print(funcion("Bea"))