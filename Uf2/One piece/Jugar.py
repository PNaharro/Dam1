import Diccionarios as Dic
import Funciones as Fun
import random
textOpts = "\n1)Crew vs Crew\n2)Crew vs Rank"
inputOptText = "Opcion: "
rangeList = [1,2]
exceptions = [0]
while True:
    opc = Fun.getOpt(textOpts,inputOptText,rangeList,exceptions)
    if opc == 1:
        print("1")
    elif opc == 2:
        print(Fun.cabecera("Crew"))
        lista_crews = []
        for i in Dic.dict_crews:
            lista_crews.append(i)
            lista = []
            for j in Dic.dict_crews[i]["members"]:
                lista.append(Dic.dict_characters[j]["name"])
            print(i,"-",Dic.dict_crews[i]["name"],"-",str(lista))
        while True:
            opc_crew = input("Elige: ")
            try:
                lista_crews.index(int(opc_crew))
                break
            except:
                print("Opcion invalida")
        print(Fun.cabecera("Rank"))
        lista_rank = []
        for i in Dic.dict_ranks:
            lista_rank.append(i)
            lista = []
            for j in Dic.dict_ranks[i]["members"]:
                lista.append(Dic.dict_characters[j]["name"])
            print(i, "-", Dic.dict_ranks[i]["name"], "-", str(lista))
        while True:
            opc_rank = input("Elige: ")
            try:
                lista_rank.index(int(opc_rank))
                break
            except:
                print("Opcion invalida")
        eleccion = random.randint(0,1)
        print(eleccion)
#########################################################
        for personaje in Dic.dict_characters:
            for j in Dic.dict_characters[personaje]["weapons"]:
                for i in Dic.dict_weapons:
                    if i == j:
                        Dic.dict_characters[personaje]["strength"] += Dic.dict_weapons[i]["strength"]
                        Dic.dict_characters[personaje]["speed"] += Dic.dict_weapons[i]["speed"]
#########################################################
        if eleccion == 0:
            print("Empieza atacando Crew")
            print(Dic.dict_crews[opc_crew]["members"])

        elif eleccion == 1:
            print("Empieza atacando Rank")

    elif opc == 0:
        print("Saliendo")
        break
print("Jugar")
