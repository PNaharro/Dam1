
while True:
    while True:
        print("Tipo de conversion:\n1)Decimal Binaria\n2)Binaria Decimal\n3)Salir")
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("Eso no es un numero")
        elif int(opc)<1 or int(opc) > 3:
            print("Numero fuera de rango")
        else:
            break
    if opc == "1":

        while True:
            ip_binario = ""
            bien = True
            ip = input("Dime la IP: ")
            for i in ip.split("."):
                if not i.isdigit():
                    bien = False
                elif int(i) < 0 or int(i) > 255:
                    bien = False
            if ip.count(".") != 3:
                bien = False
            if bien:
                break
            else:
                print("La IP esta mal formulada")
        for i in ip.split("."):
            numero = i
            ip_binario_reverse = ""
            for j in range(8):
                ip_binario_reverse = str(int(numero)%2) + ip_binario_reverse
                numero = int(numero)//2
            ip_binario += ip_binario_reverse +  "."
        print("Tu ip pasado a binario es:",ip_binario[:-1],"\n"*5)

    elif opc == "2":
        while True:
            ip_en_decimal = ""
            bien = True
            ip_en_binaio = input("Dime la IP: ")
            for j in ip_en_binaio.split("."):
                for i in j:
                    if i != "0" and i != "1":
                        bien = False
                    elif len(j) != 8:
                        bien = False
            if ip_en_binaio.count(".") != 3:
                bien = False
            if bien:
                break
            else:
                print("La IP esta mal formulada")

        ip_resultado = ""
        for i in ip_en_binaio.split("."):
            numero = 0
            for j in range(8):
                if i[j] == "1":
                    numero += 2 ** (7 - j)
            ip_resultado += str(numero) + "."
        print("Tu ip pasado a decimal es:",ip_resultado[:-1])

    else:
        print("Saliendo...")
        break