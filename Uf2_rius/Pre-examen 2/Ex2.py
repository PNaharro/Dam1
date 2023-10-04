def orden(palabra,alfabeto):
    palabra = palabra+" "
    respuesta = ""
    if palabra[0] == " ":
        return print("la palabra esta ordenada alfaveticamente")
    if palabra[0] != alfabeto[0]:
        return print("la palabra esta no ordenada alfaveticamente")
    if palabra[0] == alfabeto[0]:
        respuesta = orden(palabra[1:], alfabeto[1:])
        return respuesta

orden("an","abcdefghijklmnñopqrstuvwxyz")