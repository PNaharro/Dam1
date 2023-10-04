mario = ("Mario Gonzalez Perez","55555555E","Calle Canada 12 3º 4ª", "+0034480920459")
pedro = ("Pedro Gutierrez Lopez","66666666A","Calle Balmes 22 1º 3ª", "+0034640380192")
anabel = ("Anabel Lorca Suarez","55554444Y","Calle Vasubio 7 8º 4ª", "+0034633780192")

usuarios = [mario,pedro,anabel]


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
            nuevoUsuario = (nombre, direccion, dni, telefono)
            usuarios.append(nuevoUsuario)
        if opcion == 2:
            for u in usuarios:
                str = "Nombre: ".ljust(15)+u[0]+"\n"+"DNI: ".ljust(15)+u[1]+"\n"+"Direccion: ".ljust(15)+u[2]+"\n"+\
                    "Telefono: ".ljust(15)+u[3]
                print(str)
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
                        str = "Nombre".ljust(25)+"DNI".ljust(15)+"Direccion".ljust(25)+"Telefono".ljust(15)+\
                            "\n"+"*"*80+"\n"
                        for u in usuarios:
                            if buscar.lower() in u[0].lower():
                                str = str + u[0].ljust(25)+u[1].ljust(15)+u[2].ljust(25)+u[3].ljust(15)+"\n"
                        print(str)
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