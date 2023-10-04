# diccionario = {"clave1":"valor1" , 23:"valor2" , (2,3):"valor3" , 21: [2,3,4,(5,6,[7,8])]}
# print(diccionario[23])
# print(diccionario[(2,3)])
# print(diccionario[21])

# diccionario["clave2"] = [4,5,6]
# print(diccionario["clave2"])
# print(diccionario)
#
# diccionario["clave1"] = (5,6,7)
# print(diccionario)

#AÑADIR ELEMENTOS A UN DICCIONARIO VACIO
# diccionario = {}
# print(diccionario)
# diccionario[5] = [5,6,7]
# diccionario[6] = [5,6,7,6,7]
# diccionario["clave1"] = "valor1"
# print(diccionario)

#FORMAS DE MOSTRAR EL CONTENIDO
# for t in diccionario:
#     print(t)
# for t in diccionario:
#     print(diccionario[t])

#BORRAR UN DICCIONARIO
# del(diccionario["clave1"])
# print(diccionario)
# diccionario.clear()
# print(diccionario)

#COPIAR UN DICCIONARIO
# dic2 = diccionario.copy()
# print(dic2)


diccionario = {}

#TRANSFORMAR UNA LISA A DICCIONARIO CON VALORES
# lista = ["elemento1", "elemento2" , "elemento3"]
# lista1 = [3,4,5]
# dicc = dict.fromkeys(lista,lista1)
# print(dicc)

#SI BUSCAR UN VALOR O LLAVE QUE NO EXITE, ERROR (!!! SI USAS DICC.GET NO PETA EL PROGRAMA, DEVUELVE "NONE"!!!)
# dicc = {'elemento1': [3, 4, 5], 'elemento2': [3, 4, 5], 'elemento3': [3, 4, 5]}

#BUCSA EN DICCIONARIO
# print(dicc("elemento1"))
#BUSCAR UN VALOR NO PREDETERMINADO HARA PETAR EL PROGRAMA
# print(dicc["elemento12"])

#SI USAMOS .GET NO PETA, SOLO DEVUELVE NONE
# print(dicc.get("elemento12","valor por defecto"))

#SI USAS UNA ,"XXX" NOS DEVOLVERA EL XXX EN CASO DE NO ENCONTRAR EL ELEMENTO
# print(dicc.get("elemento12","valor por defecto"))


dicc = {'elemento1': [3, 4, 5], 'elemento2': [3, 4, 5], 'elemento3': [3, 4, 5]}

#list() ES PARA PASAR LO DE DENTRO A LISTA
#dicc.keys() SELECCIONA LAS LLAVES DEL DICCIONARIO Y dicc.values LOS VALORES
# print(list(dicc.keys()))
# print(list(dicc.values()))
# print(type(list(dicc.keys())))

#LONGITUD DE UNA LISTA
# print(len(dicc))

#CON .ITEMS SE PUEDE HACER ESTO, MAS Y MEJOR EN EL PDF
# for clave,valor in dicc.items():
#     print("clave = ", clave, "valor =",valor)

#LAS LISAS DISTINGES SUS LLAVES POR MAYUSCULAS Y MINUSCULAS
# dicc['Elemento1'] = (3,4)
# print(dicc)