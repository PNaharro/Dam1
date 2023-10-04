diccionario = {}

cosas = ("Identificador del libro: ", "Titulo: ","Autor: ","Editorial: ","Año de edicion: ", "Numero de paginas: ")

x = 0
for i in cosas:
    print(i)
    entrada = input()
    if x == 0:
        diccionario["identificador"]=entrada
    elif x == 1:
        diccionario["titulo"]=entrada
    elif x == 2:
        diccionario["autor"]=entrada
    elif x == 3:
        diccionario["titulo"]=entrada
    elif x == 4:
        diccionario["titulo"]=entrada
    elif x == 5:
        diccionario["titulo"]=entrada
    x += 1
print(diccionario.values())