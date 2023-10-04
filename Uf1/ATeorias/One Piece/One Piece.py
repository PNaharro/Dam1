dicc_players = {1:{"nombre":"Luffy","categoria":1,"armas":[1,1],"fuerza":6,"velocidad":7,"experiencia":0},
                2:{"nombre":"Zoro","categoria":1,"armas":[4],"fuerza":5,"velocidad":6,"experiencia":0},
                3:{"nombre":"Sanji","categoria":1,"armas":[1,3],"fuerza":4,"velocidad":6,"experiencia":0},
                4: {"nombre": "Buggy", "categoria": 2, "armas": [3], "fuerza": 2, "velocidad": 4, "experiencia": 0},
                5: {"nombre": "Mr3", "categoria": 2, "armas": [5], "fuerza": 3, "velocidad": 2, "experiencia": 0},
                6: {"nombre": "Xebec", "categoria": 3, "armas": [1, 3], "fuerza": 6, "velocidad": 5, "experiencia": 0},
                7: {"nombre": "Kaido", "categoria": 3, "armas": [4], "fuerza": 8, "velocidad": 3, "experiencia": 0},
                8: {"nombre": "Mama grande", "categoria": 3, "armas": [5], "fuerza": 7, "velocidad": 1, "experiencia": 0},
                9: {"nombre": "Akainu", "categoria": 4, "armas": [2], "fuerza": 6, "velocidad": 4, "experiencia": 0},
                10: {"nombre": "Kizaru", "categoria": 4, "armas": [1, 3], "fuerza": 5, "velocidad": 8, "experiencia": 0},
                11: {"nombre": "Fujitora", "categoria": 4, "armas": [5], "fuerza": 5, "velocidad": 4, "experiencia": 0},
                12: {"nombre": "Garp", "categoria": 5, "armas": [2], "fuerza": 6, "velocidad": 3, "experiencia": 0},
                13: {"nombre": "Smoker", "categoria": 5, "armas": [5], "fuerza": 5, "velocidad": 5, "experiencia": 0},
                14: {"nombre": "Koby", "categoria": 6, "armas": [4], "fuerza": 3, "velocidad": 4, "experiencia": 0},
                15: {"nombre": "Tashigi", "categoria": 6, "armas": [3], "fuerza": 4, "velocidad": 4, "experiencia": 0},
                }
dicc_weapons = {1:{"nombre":"Espada","fuerza":3,"velocidad":5,"dos_manos":False},
                2:{"nombre":"Gran Espada","fuerza":5,"velocidad":3,"dos_manos":True},
                3: {"nombre": "Pistola", "fuerza": 2, "velocidad": 6, "dos_manos": False},
                4: {"nombre": "Rifle", "fuerza": 3, "velocidad": 4, "dos_manos": True},
                5: {"nombre": "Chuchi", "fuerza": 4, "velocidad": 4, "dos_manos": True}
                }
dicc_crews = {1:{"nombre":"Straw Hat","miembros":[8,6]},
              2: {"nombre": "Pirates Buggy", "miembros": [1,3,5]},
              3: {"nombre": "Pirates Ricks", "miembros": [2,4,7]}
              }
dicc_ranks = {1:{"nombre":"Admiral","miembros":[9,10,11]},
              2:{"nombre":"ViceAdmiral","miembros":[12,13]},
              3:{"nombre":"Lieutenant","miembros":[14,15]}
              }
dicc_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}


menu0 = "="*10+"Menu 0 (One Piece)"+"="*10+"\n1)Jugar\n2)Crear\n3)Editar\n4)Listar\n5)Salir\n"
menu03 = "="*10+"Menu 03 (Editar)"+"="*10+"\n1)Editar Personaje\n2)Editar Armas\n3)Atras"
menu031 = "="*10+"Menu 031 (Seleccionar Personaje a Editar)"+"="*10+"\n"
menu032 = "="*10+"Menu 031 (Seleccionar Arma a Editar)"+"="*10+"\n"
menu04 = "="*10+"Menu 04 (Listas)"+"="*10+"\n1)Listar Personajes\n2)Listar Armas\n3)Listar Bando\n4)Listar Rango\n5)Atras\n"
menu041 = "="*10+"Menu 041 (Listar Personajes)"+"="*10+"\n1)Listar por ID\n2)Listar por Nombre\n3)Listar por Fuerza\n4)Listar por Velocidad\n5)Atras\n"
menu042 = "="*10+"Menu 042 (Listar Armas)"+"="*10+"\n1)Listar por ID\n2)Listar por Nombre\n3)Listar por Fuerza\n4)Listar por Velocidad\n5)Atras\n"
menu043 = "="*10+"Menu 043 (Listar Bandos)"+"="*10+"\n1)Listar por ID\n2)Listar por Nombre\n3)Atras\n"
menu044 = "="*10+"Menu 044 (Listar Rangos)"+"="*10+"\n1)Listar por ID\n2)Listar por Nombre\n3)Atras\n"

for i in dicc_players:
    for j in dicc_players[i]["armas"]:
        dicc_players[i]["fuerza"] += dicc_weapons[j]["fuerza"]
        dicc_players[i]["velocidad"] += dicc_weapons[j]["velocidad"]

while True:
    while True:
        print(menu0)
        opcion = input("->Opcion: ")
        if not opcion.isdigit():
            print("\n","="*5,"Valor no valido","="*5,"\n")
        elif int(opcion) < 1 or int(opcion) > 5:
            print("\n","="*5,"Valor no valido","="*5,"\n")
        else:
            opcion = int(opcion)
            break
    if opcion == 1:
        print("Jugar")
    if opcion == 2:
        print("Crear")
    if opcion == 3:
        # Menu editar
        while True:
            while True:
                # Print menu 03 + elegir opcion
                print(menu03)
                opcion = input("->Opcion: ")
                if not opcion.isdigit():
                    print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                elif int(opcion) < 1 or int(opcion) > 3:
                    print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                else:
                    opcion = int(opcion)
                    break
            if opcion == 1:
                # Editar un Personaje
                print(menu031)
                for i in dicc_players:
                    armitas = []
                    for j in dicc_players[i]["armas"]:
                        armitas.append(dicc_weapons[j]["nombre"])
                    menu0311 = "ID: {},Nombre: {}, Categoria: {}, Armas: {}, Fuerza: {}, Velocidad: {}, Experiencia: {}" \
                        .format(i, dicc_players[i]["nombre"], dicc_players[i]["categoria"], armitas,
                                dicc_players[i]["fuerza"], dicc_players[i]["velocidad"], dicc_players[i]["experiencia"])
                    print(menu0311)
                while True:
                    opcionid = input("ID del Personaje: ")
                    if not opcionid.isdigit():
                        print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                    elif int(opcionid) <= (len(dicc_players) - len(dicc_players)) or int(opcionid) > len(dicc_players):
                        print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                    else:
                        opcionid = int(opcionid)
                        break
                while True:
                    print(
                        "Selecciona la caracteristica a editar del personaje ID: {}, Nombre: {}\n\n1)Nombre\n2)Arma\n3)Atras".format(
                            opcionid, dicc_players[opcionid]["nombre"]))
                    while True:
                        opcioned = input("->Opcion: ")
                        if not opcioned.isdigit():
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        elif int(opcioned) < 1 or int(opcioned) > 3:
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        else:
                            opcioned = int(opcioned)
                            break
                    if opcioned == 1:
                        while True:
                            # Introducir nuevo nombre
                            nwnombre = input("Introduce el nuevo nombre (20 Crt):\n")
                            if not nwnombre.isalpha():
                                print("Valor no valido")
                            elif not len(nwnombre) < 20:
                                print("El nombre es demasiado largo")
                            elif not len(nwnombre) > 0:
                                print("El nombre es demasiado corto")
                            else:
                                break
                        opcion = input("Estas seguro de que quieres cambiar el nombre de {} por {}?(S/N)".format(
                            dicc_players[opcionid]["nombre"], nwnombre))
                        if opcion == "S" or opcion == "s":
                            dicc_players[opcionid]["nombre"] = nwnombre
                            print("Nombre Actualizado")
                    elif opcioned == 2:
                        print("="*10 + "Opcion no completada" + "="*10)
                    elif opcioned == 3:
                        break
            elif opcion == 2:
                # Editar un Arma
                print(menu032)
                for i in dicc_weapons:
                    menu0321 = "{}) {}, Fuerza: {}, Velocidad: {}" \
                        .format(i, dicc_weapons[i]["nombre"], dicc_weapons[i]["fuerza"], dicc_weapons[i]["velocidad"])
                    print(menu0321)
                while True:
                    opcionid = input("ID del Arma: ")
                    if not opcionid.isdigit():
                        print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                    elif int(opcionid) <= (len(dicc_weapons) - len(dicc_weapons)) or int(opcionid) > len(dicc_weapons):
                        print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                    else:
                        opcionid = int(opcionid)
                        break
                while True:
                    print("=" * 10, "Menu 032X (Caracteristica del Arma a Editar)", "=" * 10,
                          "\n\n1)Nombre\n2)Plus Fuerza\n3)Plus Velocidad\n4)Atras\nElige la caracteristica a cambiar del arma ID: {}, Nombre: {}"
                          .format(opcionid, dicc_weapons[opcionid]["nombre"]))
                    while True:
                        opcioned = input("->Opcion: ")
                        if not opcioned.isdigit():
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        elif int(opcioned) < 1 or int(opcioned) > 4:
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        else:
                            opcioned = int(opcioned)
                            break
                    if opcioned == 1:
                        while True:
                            # Introducir nuevo nombre
                            nwnombre = input("Introduce el nuevo nombre (20 Crt):\n")
                            if not nwnombre.isalpha():
                                print("Valor no valido")
                            elif not len(nwnombre) < 20:
                                print("El nombre es demasiado largo")
                            elif not len(nwnombre) > 0:
                                print("El nombre es demasiado corto")
                            else:
                                break
                        opcion = input("Estas seguro de que quieres cambiar el nombre de {} por {}?(S/N)".format(
                            dicc_weapons[opcionid]["nombre"], nwnombre))
                        if opcion == "S" or opcion == "s":
                            dicc_weapons[opcionid]["nombre"] = nwnombre
                            print("Nombre Actualizado")
                    elif opcioned == 2:
                        while True:
                            # Introducir nueva Fuerza
                            nwfuerza = input("Introduce la nueva fuerza (9 Max):\n")
                            if not nwfuerza.isdigit():
                                print("Valor no valido")
                            elif not int(nwfuerza) < 10:
                                print("Demasiada fuerza")
                            elif not int(nwfuerza) > 0:
                                print("Poca fuerza")
                            else:
                                break
                        opcion = input("Estas seguro de que quieres cambiar la fuerza de {} a {}?(S/N)".format(
                            dicc_weapons[opcionid]["fuerza"], nwfuerza))
                        if opcion == "S" or opcion == "s":
                            dicc_weapons[opcionid]["fuerza"] = nwfuerza
                            print("Fuerza Actualizada")

                    elif opcioned == 3:
                        while True:
                            # Introducir nueva Velocidad
                            nwvelocidad = input("Introduce la nueva velocidad (9 Max):\n")
                            if not nwvelocidad.isdigit():
                                print("Valor no valido")
                            elif not int(nwvelocidad) < 10:
                                print("Demasiada velocidad")
                            elif not int(nwvelocidad) > 0:
                                print("Poca velocidad")
                            else:
                                break
                        opcion = input("Estas seguro de que quieres cambiar la velocidad de {} a {}?(S/N)".format(
                            dicc_weapons[opcionid]["velocidad"], nwvelocidad))
                        if opcion == "S" or opcion == "s":
                            dicc_weapons[opcionid]["velocidad"] = nwvelocidad
                            print("Velocidad Actualizada")
                    elif opcioned == 4:
                        break
            elif opcion == 3:
                break

    if opcion == 4:
        #Elegir la opcion Listar
        while True:
            while True:
                print(menu04)
                opcion = input("->Opcion: ")
                if not opcion.isdigit():
                    print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                elif int(opcion) < 1 or int(opcion) > 5:
                    print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                else:
                    opcion = int(opcion)
                    break
            if opcion == 1:
                # Listar Personajes
                while True:
                    while True:
                        print(menu041)
                        opcion = input("->Opcion: ")
                        if not opcion.isdigit():
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        elif int(opcion) < 1 or int(opcion) > 5:
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        else:
                            opcion = int(opcion)
                            break
                    if opcion == 1:
                        # Listar por ID
                        menu0411 = "=" * 17 + "Personajes ordenados por ID" + "=" * 17 + "\n" + "ID".ljust(10) + "Nombre".ljust(15) \
                                   + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
                        print(menu0411)
                        listaID = []
                        for i in dicc_players:
                            listaID.append(i)

                        for i in range(len(listaID) - 1):
                            for j in range(len(listaID) - i - 1):
                                if listaID[j] > listaID[j + 1]:
                                    numero = listaID[j]
                                    listaID[j] = listaID[j + 1]
                                    listaID[j + 1] = numero

                        for i in listaID:
                            id = "{}".format(i).ljust(10) + dicc_players[i]["nombre"].ljust(20) + str(dicc_players[i]["fuerza"]).ljust(13) \
                                 + str(dicc_players[i]["velocidad"]).ljust(17) + str(dicc_players[i]["experiencia"])
                            print(id)
                        input()

                    elif opcion == 2:
                        #Listar por Nombre
                        menu0412 = "=" * 15 + "Personajes ordenados por Nombre" + "=" * 15 + "\n" + "ID".ljust(10) + "Nombre".ljust(15) \
                                   + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
                        print(menu0412)
                        listaName = []
                        for i in dicc_players:
                            listaName.append(dicc_players[i]["nombre"])

                        for i in range(len(listaName) - 1):
                            for j in range(len(listaName) - i - 1):
                                if listaName[j] > listaName[j + 1]:
                                    numero = listaName[j]
                                    listaName[j] = listaName[j + 1]
                                    listaName[j + 1] = numero
                        for i in listaName:
                            for j in dicc_players:
                                if i == dicc_players[j]["nombre"]:
                                    string_nombre = str("{}".format(j)).ljust(10) + str("{}".format(i)).ljust(20) + str(dicc_players[j]["fuerza"]).ljust(13) \
                                                    + str(dicc_players[j]["velocidad"]).ljust(17) + str(dicc_players[j]["experiencia"])
                                    print(string_nombre)
                        input()
                    elif opcion == 3:
                        # Listar por Fuerza
                        menu0413 = "=" * 15 + "Personajes ordenados por Fuerza" + "=" * 15 + "\n" + "ID".ljust(
                            10) + "Nombre".ljust(15) \
                                   + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
                        print(menu0413)
                        listaStg = []
                        listaKys = []
                        for i in dicc_players:
                            listaStg.append(dicc_players[i]["fuerza"])
                            listaKys.append(i)
                        for i in range(len(listaStg) - 1):
                            for j in range(len(listaStg) - i - 1):
                                if listaStg[j] < listaStg[j + 1]:
                                    numero = listaStg[j]
                                    listaStg[j] = listaStg[j + 1]
                                    listaStg[j + 1] = numero

                                    numero = listaKys[j]
                                    listaKys[j] = listaKys[j + 1]
                                    listaKys[j + 1] = numero
                        for n in listaKys:
                            string_fuerza = str("{}".format(n)).ljust(10) + str(dicc_players[n]["nombre"]).ljust(
                                20) + str(
                                dicc_players[n]["fuerza"]).ljust(13) \
                                            + str(dicc_players[n]["velocidad"]).ljust(17) + str(
                                dicc_players[n]["experiencia"])
                            print(string_fuerza)
                        input()

                    elif opcion == 4:
                        # Listar por Velocidad
                        menu0414 = "=" * 14 + "Personajes ordenados por Velocidad" + "=" * 13 + "\n" + "ID".ljust(
                            10) + "Nombre".ljust(15) \
                                   + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
                        print(menu0414)
                        listaVlz = []
                        listaKys = []
                        for i in dicc_players:
                            listaVlz.append(dicc_players[i]["velocidad"])
                            listaKys.append(i)

                        for i in range(len(listaVlz) - 1):
                            for j in range(len(listaVlz) - i - 1):
                                if listaVlz[j] < listaVlz[j + 1]:
                                    numero = listaVlz[j]
                                    listaVlz[j] = listaVlz[j + 1]
                                    listaVlz[j + 1] = numero

                                    numero = listaKys[j]
                                    listaKys[j] = listaKys[j + 1]
                                    listaKys[j + 1] = numero
                        for n in listaKys:
                            string_velocidad = str("{}".format(n)).ljust(10) + str(dicc_players[n]["nombre"]).ljust(
                                20) + str(dicc_players[n]["fuerza"]).ljust(13) \
                                               + str(dicc_players[n]["velocidad"]).ljust(17) + str(
                                dicc_players[n]["experiencia"])
                            print(string_velocidad)
                        input()
                    elif opcion == 5:
                        break

            elif opcion == 2:
                #Listar Armas
                while True:
                    while True:
                        print(menu042)
                        opcion = input("->Opcion: ")
                        if not opcion.isdigit():
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        elif int(opcion) < 1 or int(opcion) > 5:
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        else:
                            opcion = int(opcion)
                            break
                    if opcion == 1:
                        #Listar por ID
                        menu0421 = "=" * 19 + "Armas ordenados por ID" + "=" * 20 + "\n" + "ID".ljust(
                            10) + "Nombre".ljust(15) \
                                   + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "A dos manos\n" + "*" * 61
                        print(menu0421)
                        listaID = []
                        for i in dicc_weapons:
                            listaID.append(i)

                        for i in range(len(listaID) - 1):
                            for j in range(len(listaID) - i - 1):
                                if listaID[j] > listaID[j + 1]:
                                    numero = listaID[j]
                                    listaID[j] = listaID[j + 1]
                                    listaID[j + 1] = numero

                        for i in listaID:
                            if dicc_weapons[i]["dos_manos"] == True:
                                dosm = "True"
                            else:
                                dosm = "False"
                            id = "{}".format(i).ljust(10) + dicc_weapons[i]["nombre"].ljust(20) + str(
                                dicc_weapons[i]["fuerza"]).ljust(13) \
                                 + str(dicc_weapons[i]["velocidad"]).ljust(13) + dosm
                            print(id)
                        input()
                    elif opcion == 2:
                        # Listar por Nombre
                        menu0412 = "=" * 17 + "Armas ordenados por Nombre" + "=" * 18 + "\n" + "ID".ljust(10) + "Nombre".ljust(15) \
                                   + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
                        print(menu0412)
                        listaName = []
                        for i in dicc_weapons:
                            listaName.append(dicc_weapons[i]["nombre"])

                        for i in range(len(listaName) - 1):
                            for j in range(len(listaName) - i - 1):
                                if listaName[j] > listaName[j + 1]:
                                    numero = listaName[j]
                                    listaName[j] = listaName[j + 1]
                                    listaName[j + 1] = numero
                        for i in listaName:
                            for j in dicc_weapons:
                                if i == dicc_weapons[j]["nombre"]:
                                    if dicc_weapons[j]["dos_manos"] == True:
                                        dosm = "True"
                                    else:
                                        dosm = "False"
                                    string_nombre = str("{}".format(j)).ljust(10) + str("{}".format(i)).ljust(20) + str(dicc_weapons[j]["fuerza"]).ljust(13) + str(dicc_weapons[j]["velocidad"]).ljust(13) + dosm
                                    print(string_nombre)
                        input()
                    elif opcion == 3:
                        #Listar por Fuerza
                        menu0423 = "=" * 17 + "Armas ordenados por Fuerza" + "=" * 18 + "\n" + "ID".ljust(
                            10) + "Nombre".ljust(15) \
                                   + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "A dos manos\n" + "*" * 61
                        print(menu0423)
                        listaStg = []
                        listaKys = []

                        for i in dicc_weapons:
                            listaStg.append(dicc_weapons[i]["fuerza"])
                            listaKys.append(i)

                        for i in range(len(listaStg) - 1):
                            for j in range(len(listaStg) - i - 1):
                                if listaStg[j] < listaStg[j + 1]:
                                    numero = listaStg[j]
                                    listaStg[j] = listaStg[j + 1]
                                    listaStg[j + 1] = numero

                                    numero = listaKys[j]
                                    listaKys[j] = listaKys[j + 1]
                                    listaKys[j + 1] = numero

                        for n in listaKys:
                            if dicc_weapons[n]["dos_manos"] == True:
                                dosm = "True"
                            else:
                                dosm = "False"
                            string_stg = str("{}".format(n)).ljust(10) + str(dicc_weapons[n]["nombre"]).ljust(20) + str(
                                dicc_weapons[n]["fuerza"]).ljust(13) \
                                         + str(dicc_weapons[n]["velocidad"]).ljust(13) + dosm
                            print(string_stg)
                        input()
                    elif opcion == 4:
                        #Listar por Velocidad
                        menu0424 = "=" * 17 + "Armas ordenados por Velocidad" + "=" * 18 + "\n" + "ID".ljust(10) + "Nombre".ljust(15) \
                                   + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "A dos manos\n" + "*" * 61
                        print(menu0424)
                        listaVlz = []
                        listaKys = []

                        for i in dicc_weapons:
                            listaVlz.append(dicc_weapons[i]["fuerza"])
                            listaKys.append(i)

                        for i in range(len(listaVlz) - 1):
                            for j in range(len(listaVlz) - i - 1):
                                if listaVlz[j] > listaVlz[j + 1]:
                                    numero = listaVlz[j]
                                    listaVlz[j] = listaVlz[j + 1]
                                    listaVlz[j + 1] = numero

                                    numero = listaKys[j]
                                    listaKys[j] = listaKys[j + 1]
                                    listaKys[j + 1] = numero

                        for n in listaKys:
                            if dicc_weapons[n]["dos_manos"] == True:
                                dosm = "True"
                            else:
                                dosm = "False"
                            string_vlc = str("{}".format(n)).ljust(10) + str(dicc_weapons[n]["nombre"]).ljust(20) + str(dicc_weapons[n]["fuerza"]).ljust(13) \
                                         + str(dicc_weapons[n]["velocidad"]).ljust(13) + dosm
                            print(string_vlc)
                        input()
                    elif opcion == 5:
                        break
            elif opcion == 3:
                # Listar Bandos
                while True:
                    while True:
                        print(menu043)
                        opcion = input("->Opcion: ")
                        if not opcion.isdigit():
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        elif int(opcion) < 1 or int(opcion) > 5:
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        else:
                            opcion = int(opcion)
                            break
                    if opcion == 1:
                        #Listar por ID
                        menu0431 = "=" * 19 + "Bandos ordenador por ID" + "=" * 19 + "\n" + "ID".ljust(
                            10) + "Nombre".ljust(20) + "Miembros".ljust(10) + "\n"+ "*" * 61
                        print(menu0431)
                        for i in dicc_crews:
                            cadenambr = ""
                            for j in dicc_crews[i]["miembros"]:
                                cadenambr = cadenambr + str(dicc_players[j]["nombre"]) + "\n".ljust(31)
                                string_bando = str("{}".format(i)).ljust(10) + str(dicc_crews[i]["nombre"]).ljust(
                                    20) + str(cadenambr).ljust(13)
                            print(string_bando)
                        input()
                    elif opcion == 2:
                        #Listar por Nombre
                        menu0432 = "=" * 17 + "Bandos ordenador por Nombre" + "=" * 17 + "\n" + "ID".ljust(
                            10) + "Nombre".ljust(20) + "Miembros".ljust(10) + "\n" + "*" * 61
                        print(menu0432)
                        listaCrew = []
                        for i in dicc_crews:
                            listaCrew.append(dicc_crews[i]["nombre"])

                        for i in range(len(listaCrew) - 1):
                            for j in range(len(listaCrew) - i - 1):
                                if listaCrew[j] > listaCrew[j + 1]:
                                    numero = listaCrew[j]
                                    listaCrew[j] = listaCrew[j + 1]
                                    listaCrew[j + 1] = numero

                        for i in listaCrew:
                            for j in dicc_crews:
                                if i == dicc_crews[j]["nombre"]:
                                    cadenaid = ""
                                    for x in dicc_crews[j]["miembros"]:
                                        cadenaid = cadenaid + str(dicc_players[x]["nombre"]) + "\n".ljust(31)
                                        string_bando = str("{}".format(j)).ljust(10) + str(dicc_crews[j]["nombre"]).ljust(
                                            20) + str(cadenaid).ljust(13)
                                    print(string_bando)
                        input()
                    elif opcion == 3:
                        break

            elif opcion == 4:
                # Listar Rangos
                while True:
                    while True:
                        print(menu044)
                        opcion = input("->Opcion: ")
                        if not opcion.isdigit():
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        elif int(opcion) < 1 or int(opcion) > 5:
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        else:
                            opcion = int(opcion)
                            break
                    if opcion == 1:
                        #Listar por ID
                        menu0441 = "=" * 19 + "Rangos ordenador por ID" + "=" * 19 + "\n" + "ID".ljust(
                            10) + "Nombre".ljust(20) + "Miembros".ljust(10) + "\n"+ "*" * 61
                        print(menu0441)
                        for i in dicc_ranks:
                            cadenambr = ""
                            for j in dicc_ranks[i]["miembros"]:
                                cadenambr = cadenambr + str(dicc_players[j]["nombre"]) + "\n".ljust(31)

                                string_rango = str("{}".format(i)).ljust(10) + str(dicc_ranks[i]["nombre"]).ljust(
                                    20) + str(cadenambr).ljust(13)
                            print(string_rango)
                        input()
                    elif opcion == 2:
                        # Listar por ID
                        menu0442 = "=" * 17 + "Rangos ordenador por Nombre" + "=" * 17 + "\n" + "ID".ljust(
                            10) + "Nombre".ljust(20) + "Miembros".ljust(10) + "\n" + "*" * 61
                        print(menu0442)
                        listaRangos = []
                        for i in dicc_ranks:
                            listaRangos.append(dicc_ranks[i]["nombre"])

                        for i in range(len(listaRangos) - 1):
                            for j in range(len(listaRangos) - i - 1):
                                if listaRangos[j] > listaRangos[j + 1]:
                                    numero = listaRangos[j]
                                    listaRangos[j] = listaRangos[j + 1]
                                    listaRangos[j + 1] = numero

                        for i in listaRangos:
                            for j in dicc_ranks:
                                if i == dicc_ranks[j]["nombre"]:
                                    cadenaid = ""
                                    for x in dicc_ranks[j]["miembros"]:
                                        cadenaid = cadenaid + str(dicc_players[x]["nombre"]) + "\n".ljust(31)
                                        string_rango = str("{}".format(j)).ljust(10) + str(dicc_ranks[j]["nombre"]).ljust(
                                            20) + str(cadenaid).ljust(13)
                                    print(string_rango)
                        input()
                    elif opcion == 3:
                        break
            elif opcion == 5:
                break

    elif opcion == 5:
        break