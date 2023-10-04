import math
menu = "*"*15+"Calculos de vectores"+"*"*15+"\n"+"1. Introducir el primer vector\n2. Introducir el segundo vector" \
        "\n3. Calcular la suma\n4. Calcular la diferencia\n5. Calcular el producto escalar\n" \
        "6. Calcular el producto vectorial\n7. Calcular el angulo (en grados) entre ellos\n8. Calcular la longitud" \
        "\n9. Finalizar"

confirmante1 = 0
confirmante2 = 0
while True:
    print(menu)
    while True:
        opcion = input("->Opcion: ")
        if opcion.isdigit()==False:
            print("Por un numero para elegir la opcion")
        elif int(opcion)<1 or int(opcion)>9:
            print("Pon un numero valido")
        else:
            opcion = int(opcion)
            break
    if opcion == 1:
        while True:
            x1 = input("Introduce x1: ")
            y1 = input("Introduce y1: ")
            z1 = input("Introduce z1: ")
            if x1.isdigit()==False or y1.isdigit()==False or z1.isdigit()==False:
                print("Coloca bien los numeros")
            else:
                x1 = int(x1)
                y1 = int(y1)
                z1 = int(z1)
                confirmante1 = 1
                break
    elif opcion == 2:
        while True:
            x2 = input("Introduce x2: ")
            y2 = input("Introduce y2: ")
            z2 = input("Introduce z2: ")
            if x2.isdigit() == False or y2.isdigit() == False or z2.isdigit() == False:
                print("Coloca bien los numeros")
            else:
                x2 = int(x2)
                y2 = int(y2)
                z2 = int(z2)
                confirmante2 = 1
                break
    elif opcion == 3:
        if confirmante1 == 0 and confirmante2 == 0:
            print("Porfavor, inserta los vectores")
            input("Pulsa para continuar")
        elif confirmante1 == 0:
            print("Porfavor, inserta el primer vector")
            input("Pulsa para continuar")
        elif confirmante2 == 0:
            print("Porfavor, inserta el segundo vector")
            input("Pulsa para continuar")
        else:
            input("Pulsa para hacer la suma")
            suma = (x1+x2,y1+y2,z1+z2)
            print("X: {}\nY: {}\nZ: {}".format(suma[0],suma[1],suma[2]))
            input()
    elif opcion == 4:
        if confirmante1 == 0 and confirmante2 == 0:
            print("Porfavor, inserta los vectores")
            input("Pulsa para continuar")
        elif confirmante1 == 0:
            print("Porfavor, inserta el primer vector")
            input("Pulsa para continuar")
        elif confirmante2 == 0:
            print("Porfavor, inserta el segundo vector")
            input("Pulsa para continuar")
        else:
            while True:
                resta_opc = input("Quieres hacer x1 - x2 (pulsa 1) o x2 - x1 (pulsa 2): ")
                if resta_opc == "1":
                    input("Pulsa para hacer la diferencia")
                    resta = (x1 - x2, y1 - y2, z1 - z2)
                    print("X: {}\nY: {}\nZ: {}".format(resta[0], resta[1], resta[2]))
                    input()
                    break
                elif resta_opc == "2":
                    input("Pulsa para hacer la diferencia")
                    resta = (x2 - x1, y2 - y1, z2 - z1)
                    print("X: {}\nY: {}\nZ: {}".format(resta[0], resta[1], resta[2]))
                    input()
                    break
                else:
                    print("Inserta un valor valido")
    elif opcion == 5:
        if confirmante1 == 0 and confirmante2 == 0:
            print("Porfavor, inserta los vectores")
            input("Pulsa para continuar")
        elif confirmante1 == 0:
            print("Porfavor, inserta el primer vector")
            input("Pulsa para continuar")
        elif confirmante2 == 0:
            print("Porfavor, inserta el segundo vector")
            input("Pulsa para continuar")
        else:
            input("Pulsa para hacer el producto escalar")
            producto_e = ((x1 * x2) + (y1 * y2) + (z1 * z2))
            print("El resultado es {}".format(producto_e))
            input()
    elif opcion == 6:
        if confirmante1 == 0 and confirmante2 == 0:
            print("Porfavor, inserta los vectores")
            input("Pulsa para continuar")
        elif confirmante1 == 0:
            print("Porfavor, inserta el primer vector")
            input("Pulsa para continuar")
        elif confirmante2 == 0:
            print("Porfavor, inserta el segundo vector")
            input("Pulsa para continuar")
        else:
            while True:
                vectorial_opc = input("Quieres hacer y1z2 - z1y2 (pulsa 1) o z1y2 - y1z2 (pulsa 2): ")
                if vectorial_opc == "1":
                    input("Pulsa para hacer el producto vectorial")
                    producto_v = ((y1*z2)-(z1*y2),(z1*x2)-(x1*z2),(x1*y2)-(y1*x2))
                    print("1o: {}\n2o: {}\n3o: {}".format(producto_v[0], producto_v[1], producto_v[2]))
                    input()
                    break
                elif vectorial_opc == "2":
                    input("Pulsa para hacer el producto vectorial")
                    producto_v = ((z1*y2)-(y1*z2),(x1*z2)-(z1*x2),(y1*x2)-(x1*y2))
                    print("1o: {}\n2o: {}\n3o: {}".format(producto_v[0], producto_v[1], producto_v[2]))
                    input()
                    break
                else:
                    print("Inserta un valor valido")
#############################################################################################################################################################
    elif opcion == 7:
        operacion1 = (x1*x2)+(y1*y2)+(z1*z2)

        operacion20 = (x1**2)+(y1**2)+(z1**2)
        if operacion20 >= 0:
            p20 = operacion20
            i20 = 0
            while i20 != p20:
                i20 = p20
                p20 = (operacion20 / p20 + p20) / 2
                operacion21 = p20
        else:
            print("La operacion no es posible")

        operacion30 = (x2**2)+(y1**2)+(z2**2)
        if operacion30 >= 0:
            p30 = operacion30
            i30 = 0
            while i30 != p30:
                i30 = p30
                p30 = (operacion30 / p30 + p30) / 2
                operacion31 = p30
        else:
            print("La operacion no es posible")

        operacion50 = operacion21 * operacion31
        operacion100 = operacion1/operacion50

        operacion = (180/math.pi)*math.acos(operacion100)
#############################################################################################################################################################
    elif opcion == 8:
        if confirmante1 == 0 and confirmante2 == 0:
            print("Porfavor, inserta los vectores")
            input("Pulsa para continuar")
        elif confirmante1 == 0:
            print("Porfavor, inserta el primer vector")
            input("Pulsa para continuar")
        elif confirmante2 == 0:
            print("Porfavor, inserta el segundo vector")
            input("Pulsa para continuar")
        else:
            longitud = input("Quieres hacer raiz cuadrada de la suma de x1, y1 y z1 (pulsa 1) o de x2, y2 y z2 (pulsa 2): ")
            if longitud == "1":
                operacion = (x1**2)+(y1**2)+(z1**2)
                if operacion >= 0:
                    p = operacion
                    i = 0
                    while i != p:
                        i = p
                        p = (operacion / p + p) / 2
                        input("Pulsa para hacer la longitud")
                    print("Resultados es: ", p)
                else:
                    print("La operacion no es posible")
                    input()
                break
            elif longitud == "2":
                operacion = (x2**2)+(y2**2)+(z2**2)
                if operacion >= 0:
                    p = operacion
                    i = 0
                    while i != p:
                        i = p
                        p = (operacion / p + p) / 2
                        input("Pulsa para hacer la longitud")
                    print("Resultados es: ", p)
                else:
                    print("La operacion no es posible")
                    input()
                break
            else:
                print("Inserta un valor valido")
    elif opcion == 9:
        print("Cerrando programa...")
        break