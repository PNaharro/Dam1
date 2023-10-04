import Diccionarios as Dic

def cabecera(text):
    x = (100-len(text))/2
    y = 100
    if len(text)%2!=0:
        y -= 1
    cadena = "*"*y +"\n" + "="*int(x) + text + "="*int(x) + "\n" + "*"*y
    return cadena

def ordenar_lista(lista,orden):
    if orden == "asc":
        for i in range(len(lista) - 1):
            for j in range(len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    numero = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = numero
    elif orden == "des":
        for i in range(len(lista) - 1):
            for j in range(len(lista) - i - 1):
                if lista[j] < lista[j + 1]:
                    numero = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = numero
    return lista
lista = [2,3,1,5]
#print(ordenar_lista(lista,"des"))

def getOpt(textOpts,inputOptText,rangeList,exceptions):
    while True:
        print(textOpts)
        opc = input(inputOptText)
        if not opc.isdigit():
            opc = len(rangeList)+1
        for i in exceptions:
            if type(i) == int:
                if int(opc) == i:
                    return int(opc)
            else:
                if opc == i:
                    return opc

        for i in rangeList:
            if int(opc) == i:
               return int(opc)
        print("Valor no valido")
        input()
def getOpt_menuprincipal(textOpts,inputOptText,rangeList,exceptions):
    while True:
        print(cabecera("Menu One Piece"))
        print(textOpts)
        opc = input(inputOptText)
        if not opc.isdigit():
            opc = len(rangeList)+1
        for i in exceptions:
            if type(i) == int:
                if int(opc) == i:
                    return "0"
            else:
                if opc == i:
                    return "-1"

        for i in rangeList:
            if int(opc) == i:
               return int(opc)
        print("Valor no valido")
        input()

#######################
def cabecera_headerDictCharactersTable(text):
    x = (60 -len(text))/2
    y = 60
    if len(text)%2!=0:
        y -= 1
    cadena = "="*int(x) + text + "="*int(x)
    return cadena

def headerDictCharactersTable(t_name_columns,t_size_columns,title):
    cadena = cabecera_headerDictCharactersTable(title) + "\n"
    for i in t_name_columns[:2]:
            cadena += i.ljust(t_size_columns[0])
            t_size_columns = t_size_columns[1:]
    for j in t_name_columns[2:]:
            cadena += j.rjust(t_size_columns[0])
            t_size_columns = t_size_columns[1:]
    cadena += "\n" + "*" * 60
    return cadena

def cabecera_headerDictWeaponsTable(text):
    x = (60 -len(text))/2
    y = x
    if len(text)%2!=0:
        y += 1
    cadena = "="*int(x) + text + "="*int(y)
    return cadena

def headerDictWeaponsTable(t_name_columns,t_size_columns,title):
    cadena = cabecera_headerDictWeaponsTable(title) + "\n"
    for i in t_name_columns[:2]:
            cadena += i.ljust(t_size_columns[0])
            t_size_columns = t_size_columns[1:]
    for j in t_name_columns[2:]:
            cadena += j.rjust(t_size_columns[0])
            t_size_columns = t_size_columns[1:]
    cadena += "\n" + "*" * 60
    return cadena

