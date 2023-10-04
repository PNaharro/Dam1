menu00 = "*"*10 + "Menu0" + "*"*10 + "\n1)Menu01\n2)Menu02\n3)Exit"
menu01 = "*"*10 + "Menu01" + "*"*10 + "\n1)Menu011\n2)Menu012\n3)Back"
menu02 = "*"*10 + "Menu02" + "*"*10 + "\n1)Menu021\n2)Menu022\n3)Back"
menu011 = "*"*10 + "Menu011" + "*"*10 + "\n1)Menu0111\n2)Menu0112\n3)Back"
menu012 = "*"*10 + "Menu012" + "*"*10 + "\n1)Menu0121\n2)Menu0122\n3)Back"
menu021 = "*"*10 + "Menu021" + "*"*10 + "\n1)Menu0211\n2)Menu0212\n3)Back"
menu022 = "*"*10 + "Menu022" + "*"*10 + "\n1)Menu0221\n2)Menu0222\n3)Back"

flag00 = True
flag01 = False
flag02 = False
flag011 = False
flag012 = False
flag021 = False
flag022 = False

#Entra al menu00
while flag00:
    print(menu00)
    while True:
        opcion = input("->Opcion: ")
        if opcion.isdigit() == False:
            print("Introduce un dijito")
        else:
            break
    if opcion == "1":
        flag01 = True
        flag00 = False
    elif opcion == "2":
        flag02 = True
        flag00 = False
    else:
        print("Cerrando programa...")
        break
#Entra al menu01
    while flag01:
        print(menu01)
        while True:
            opcion = input("->Opcion: ")
            if opcion.isdigit() == False:
                print("Introduce un dijito")
            else:
                break
        if opcion == "1":
            flag01 = False
            flag011 = True
        elif opcion == "2":
            flag01 = False
            flag012 = True
        elif opcion == "3":
            flag01 = False
            flag00 = True
#Entrar al menu011
        while flag011:
            print(menu011)
            while True:
                opcion = input("->Opcion: ")
                if opcion.isdigit() == False:
                    print("Introduce un dijito")
                else:
                    break
            if opcion == "1":
                print("Estas en el menu 0111")
                break
            elif opcion == "2":
                print("Estas en el menu 0112")
                break
            elif opcion == "3":
                flag011 = False
                flag01 = True
#Entra al menu 012
        while flag012:
            print(menu012)
            while True:
                opcion = input("->Opcion: ")
                if opcion.isdigit() == False:
                    print("Introduce un dijito")
                else:
                    break
            if opcion == "1":
                print("Estas en el menu 0121")
                break
            elif opcion == "2":
                print("Estas en el menu 0122")
                break
            elif opcion == "3":
                flag012 = False
                flag01 = True
#Entra al menu02
    while flag02:
        print(menu02)
        while True:
            opcion = input("->Opcion: ")
            if opcion.isdigit() == False:
                print("Introduce un dijito")
            else:
                break
        if opcion == "1":
            flag02 = False
            flag021 = True
        elif opcion == "2":
            flag02 = False
            flag022 = True
        elif opcion == "3":
            flag02 = False
            flag00 = True
#Entra al menu 021
        while flag021:
            print(menu021)
            while True:
                opcion = input("->Opcion: ")
                if opcion.isdigit() == False:
                    print("Introduce un dijito")
                else:
                    break
            if opcion == "1":
                print("Estas en el menu 0211")
                break
            elif opcion == "2":
                print("Estas en el menu 0212")
                break
            elif opcion == "3":
                flag021 = False
                flag02 = True
#Entra al menu 022
        while flag022:
            print(menu022)
            while True:
                opcion = input("->Opcion: ")
                if opcion.isdigit() == False:
                    print("Introduce un dijito")
                else:
                    break
            if opcion == "1":
                print("Estas en el menu 0221")
                break
            elif opcion == "2":
                print("Estas en el menu 0222")
                break
            elif opcion == "3":
                flag022 = False
                flag02 = True