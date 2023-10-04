def prueba():
    while True:
        nombre = input("Dime un nombre de usuario: ")
        if not len(nombre)>5:
            print("El nom d'usuari ha de contenir almenys 6 caràcters")
        elif not len(nombre)<13:
            print("El nom d'usuari no pot contenir més de 12 caràcters")
        elif nombre.isdigit() or nombre.isalpha():
            print("El nom d'usuari pot contenir només lletres i números")
        elif not nombre.isalnum():
            print("El nombre no puede contener ni caracteres especiales ni espacios")
        elif nombre.isalnum():
            print("True")
            break

def comprobante_contraseña():
    while True:
        contraseña = input("Dime tu contraseña: ")
        if len(contraseña) < 8:
            print("La contrasenya triada no és segura")
        elif len(contraseña)>=8:
            num = 0
            may = 0
            min = 0
            not_alnum = 0
            blanco = 0
            for i in contraseña:
                if i.isdigit():
                    num+=1
                elif i.islower():
                    min+=1
                elif i.isupper():
                    may+=1
                elif i.isspace():
                    blanco+=1
                elif not i.isalnum():
                    not_alnum+=1
            if num == 0:
                print("La contrasenya triada no és segura")
            elif may == 0:
                print("La contrasenya triada no és segura")
            elif min == 0:
                print("La contrasenya triada no és segura")
            elif not_alnum == 0:
                print("La contrasenya triada no és segura")
            elif blanco >=1:
                print("La contrasenya triada no és segura")
            else:
                print("True")
                break

