# mario = ("Mario Gonzalez Perez","55555555E","Calle Canada 12 3º 4ª", "+0034480920459")
# pedro = ("Pedro Gutierrez Lopez","66666666A","Calle Balmes 22 1º 3ª", "+0034640380192")
# anabel = ("Anabel Lorca Suarez","55554444Y","Calle Vasubio 7 8º 4ª", "+0034633780192")
#
mario = {"nombre":"Mario Gonzalez Perez","direccion":"Canada 12 3º 4ª","tfn":["+0034480920459","+0034411111111"]}
pedro = {"nombre":"Pedro Gutierrez Lopez","direccion":"Balmes 22 1º 3ª","tfn":["+0034640380192","+0034422222222"]}
anabel = {"nombre":"Anabel Lorca Suarez","direccion":"Vasubio 7 8º 4ª","tfn":["+0034633780192","+0034480123459"]}
# usuarios = [mario,pedro,anabel]

usuarios = {"55554444Y":anabel ,"66666666A":pedro,"55555555E":mario}

lestrasDNI = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

while True:
    print("********Gestoria de Usuarios********")
    print("1)Nuevo usuario\n2)Listar usuario\n3)Buscar\n4)Salir")
    opcion = input("Opcion: ")
    if not opcion.isdigit():
        print("Opcion no valida")
    elif int(opcion)<1 or int(opcion)>4:
        print("Opcion no valida")
    else:
        opcion = int(opcion)
        if opcion == 1:
            print("Nuevo usuario:\n")
            nombre = input("Nombre del nuevo usuario: \n")
            direccion = input("Direccion del nuevo usuario: \n")
            while True:
                dni = input("DNI del nuevo usuario: \n")
                if len(dni) != 9 or not dni[0:8].isdigit():
                    print("Coloca bien el DNI")
                elif lestrasDNI[int(dni[0:8]) % 23].lower != dni[8].lower:
                    print("La letra del DNI es incorrecta")
                else:
                    print("Todo piola")
                    break
            while True:
                telefono = input("Telefono nuevo usuario: \n")
                if len(telefono) != 14 or not telefono[1:].isdigit():
                    print("Formato del telefono incorrecto.")
                elif telefono[0] != "+":
                    print("Formato del telefono incorrecto:")
                else:
                    print("Telefono correcto")
                    break
#Meter aqui {"nombre":"Mario Gonzalez Perez","direccion":"Calle Canada 12 3º 4ª","tfn":["+0034480920459"]}
            nuevoUsuario = {"nombre":nombre,"tfn":[telefono], "direccion":direccion}
            usuarios[dni] = nuevoUsuario
            print(usuarios)
        if opcion == 2:
            while True:
                print("0)Listar por DNI\n1)Listar por nombre\n2)Listar por direccion\n3)Salir")
                opcion = input("Opcion: ")
                if not opcion.isdigit():
                    print("Opcion no valida")
                elif int(opcion) < 0 or int(opcion)>3:
                    print("Opcion no valida")
                else:
                    opcion = int(opcion)
                    if opcion == 0:

                        listadni = list(usuarios.keys())
                        for i in range(len(listadni)-1):
                            for j in range(len(listadni)-i-1):
                                if listadni[j] > listadni[j+1]:
                                    listadni[j] , listadni[j+1] = listadni[j+1] , listadni[j]


                        cadena = "Nombre".ljust(25) + "DNI".ljust(15) + "Direccion".ljust(25) + "Telefono".ljust(15)+"\n"+"~"*85+"\n"
                        for dni in listadni:
                            cadenatfn = ""
                            for tfn in usuarios[dni]["tfn"]:
                                cadenatfn = cadenatfn + tfn + "\n".ljust(66)
                            cadena = cadena + usuarios[dni]["nombre"].ljust(25) + dni.ljust(15) + usuarios[dni]["direccion"].ljust(25) + \
                                     cadenatfn+"\n"
                        print(cadena)
                        input()

                    if opcion == 1:
                        listadni = list(usuarios.keys())
                        for i in range(len(listadni) - 1):
                            for j in range(len(listadni) - i - 1):
                                if usuarios[listadni[j]]["nombre"] > usuarios[listadni[j+1]]["nombre"]:
                                    listadni[j], listadni[j + 1] = listadni[j + 1], listadni[j]
                        cadena = "Nombre ".ljust(25) + "DNI ".ljust(15) + "Dirección ".ljust(30) + "tfn ".ljust(
                            15) + "\n" + "*"*80 + "\n"
                        for dni in listadni:
                            cadenatfn = ""
                            for tfn in usuarios[dni]["tfn"]:
                                cadenatfn = cadenatfn + tfn + "\n" + " ".ljust(70)
                            cadena = cadena + usuarios[dni]["nombre"].ljust(25) + dni.ljust(15) + usuarios[dni][
                                "direccion"].ljust(30) + cadenatfn.ljust(70) + "\n"
                        print(cadena)
                        input()

                    if opcion == 2:
                        listadni = list(usuarios.keys())
                        for i in range(len(listadni) - 1):
                            for j in range(len(listadni) - i - 1):
                                if usuarios[listadni[j]]["direccion"] > usuarios[listadni[j + 1]]["direccion"]:
                                    listadni[j], listadni[j + 1] = listadni[j + 1], listadni[j]
                        cadena = "Nombre ".ljust(25) + "DNI ".ljust(15) + "Dirección ".ljust(30) + "tfn ".ljust(
                            15) + "\n" + "*" * 80 + "\n"
                        for dni in listadni:
                            cadenatfn = ""
                            for tfn in usuarios[dni]["tfn"]:
                                cadenatfn = cadenatfn + tfn + "\n" + " ".ljust(70)
                            cadena = cadena + usuarios[dni]["nombre"].ljust(25) + dni.ljust(15) + usuarios[dni][
                                "direccion"].ljust(30) + cadenatfn.ljust(70) + "\n"
                        print(cadena)
                        input()
                    if opcion == 3:
                        break
            input()
        if opcion == 3:
            while True:
                print("********Menu Buscar********")
                print("1)Nombre\n2)DNI\n3)Telefono\n4)Salir")
                opcion = input("Opcion: ")
                if not opcion.isdigit():
                    print("Opcion no valida")
                elif int(opcion) < 1 or int(opcion) > 4:
                    print("Opcion no valida")
                else:
                    opcion = int(opcion)
                    if opcion == 1:
                        buscar = input("Nombre a buscar: ")
                        cadena = "Nombre".ljust(25)+"DNI".ljust(15)+"Direccion".ljust(25)+"Telefonos".ljust(15)+\
                            "\n"+"*"*80+"\n"
                        for u in usuarios:
                            if buscar.lower() in usuarios[u]["nombre"].lower():
                                cadena = cadena+ usuarios[u]["nombre"].ljust(25)+u.ljust(15)+usuarios[u]["direccion"].ljust(25)+str(usuarios[u]["tfn"])+"\n"
                        print(cadena)
                        input()
                    if opcion == 2:
                        buscar = input("DNI a buscar: ")
                        str = "Nombre".ljust(25) + "DNI".ljust(15) + "Direccion".ljust(25) + "Telefono".ljust(15) + \
                              "\n" + "*" * 80 + "\n"
                        for u in usuarios:
                            if buscar.lower() in u[1].lower():
                                str = str + u[0].ljust(25) + u[1].ljust(15) + u[2].ljust(25) + u[3].ljust(15) + "\n"
                        print(str)
                        input()
                    if opcion == 3:
                        buscar = input("Telefono a buscar: ")
                        str = "Nombre".ljust(25) + "DNI".ljust(15) + "Direccion".ljust(25) + "Telefono".ljust(15) + \
                              "\n" + "*" * 80 + "\n"
                        for u in usuarios:
                            if buscar.lower() in u[3].lower():
                                str = str + u[0].ljust(25) + u[1].ljust(15) + u[2].ljust(25) + u[3].ljust(15) + "\n"
                        print(str)
                        input()
                    if opcion == 4:
                        opcion = 0
                        break
        if opcion == 4:
            break