menu = "\nTipo de conversion:\n1)Hexadecimal Binaria\n2)Binaria Hexadecimal\n3)Salir"
listahexa = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
while True:
    cadena = ""
    print(menu)
    while True:
        x = input("->Opcion: ")
        if x.isalpha() or int(x) < 1 or int(x)>3:
            print("Introduce un valor valido")
        else:
            break
    if x == "1":
        while True:
            MAC = input("Introduce la MAC: ")
            listaMAC = []
            mac = ""
            MAC = MAC.upper()
            for i in MAC:
                if not i == ":":
                    mac = mac + i
                if len(mac) == 2:
                    listaMAC.append(mac)
                    mac=""
            if len(listaMAC)!=6:
                print("MAC no valdia")
            else:
                break
        for x in listaMAC:
            resultado = 0
            for i in range(len(x)):
                resultado = resultado + listahexa.index(x[i])*16**(len(x)-1-i)
            octetoBin = ""
            for i in range(8):
                octetoBin = str(resultado%2) + octetoBin
                resultado = resultado//2
            cadena = cadena + octetoBin + ":"
        cadena = cadena[:-1]
        print("El numero binario es = ", cadena)

    elif x == "2":
        x = input("Dime el binario: ")
        binario = x.split(":")
        for x in binario:
            resultado = 0
            for i in range(len(x)):
                resultado += int(x[i]) * 2 ** int((len(x) - 1 - i))
                cadena1 = ""
            for i in range(2):
                cadena1 = str(listahexa[resultado % 16]) + cadena1
                resultado = resultado // 16
            cadena = cadena + cadena1
            cadena = cadena + ":"
        cadena = cadena[:-1]
        print("El hexadecimal es ", cadena)
    elif x == "3  ":
        break