bando = "Elije el bando de tu personaje\n1)Alianza\n2)Horda\n3)Resetear Nombre"
alianza = "Elije la raza de tu personaje\n1)Humano\n2)Enano\n3)Resetear Bando\n4)Resetear Personaje"
humano = "Elije tu arma\n1)Ballesta\n2)Espada\n3)Resetear Raza\n4)Resetear Bando\n5)Resetear Personaje"
enano = "Elije tu arma\n1)Maretillo de Guerra\n2)Trabuco\n3)Resetear Raza\n4)Resetear Bando\n5)Resetear Personaje"
horda = "Elije la raza de tu personaje\n1)Orco\n2)No Muerto\n3)Resetear Bando\n4)Resetear Personaje"
orco = "Elije tu arma\n1)Maza\n2)Martillo de guerra\n3)Resetear Raza\n4)Resetear Bando\n5)Resetear Personaje"
no_muerto = "Elije tu arma\n1)Baston\n2)Espada\n3)Resetear Raza\n4)Resetear Bando\n5)Resetear Personaje"

final = False
flag_0 = True
flag_00 = True
bando_01 = False
#Alianza
alianza_010 = False
humano_011 = False
enano_012 = False
#Horda
horda_020 = False
orco_021 = False
no_muerto_022 = False

while flag_0:
    while flag_00:
        nombre = input("Elije el nombre de tu personaje:\n")
        flag_00 = False
        bando_01 = True

    while bando_01:
        print(bando)
        opcion = input()
        if opcion == "1":
            bando_01 = False
            alianza_010 = True
            sel_bando = "Alianza"
        elif opcion == "2":
            bando_01 = False
            horda_020 = True
            sel_bando = "Horda"
        elif opcion == "3":
            bando_01 = False
            flag_00 = True
        else:
            input("Porfavor pulse un numero valudo")

    while alianza_010:
        print(alianza)
        opcion = input()
        if opcion == "1":
            alianza_010 = False
            humano_011 = True
            sel_alianza = "Humana"
        elif opcion == "2":
            alianza_010 = False
            enano_012 = True
            sel_alianza = "Enano"
        elif opcion == "3":
            alianza_010 = False
            bando_01 = True
        elif opcion == "4":
            alianza_010 = False
            flag_00 = True
        else:
            input("Porfavor pulse un numero valudo")

    while humano_011:
        print(humano)
        opcion = input()
        if opcion == "1":
            sel_arma = "Balleta"
            humano_011 = False
            final = True
        elif opcion == "2":
            sel_arma = "Espada"
            humano_011 = False
            final = True
        elif opcion == "3":
            humano_011 = False
            alianza_010 = True
        elif opcion == "4":
            humano_011 = False
            bando_01 = True
        elif opcion == "5":
            humano_011 = False
            flag_00 = True
        else:
            input("Porfavor pulse un numero valudo")

    while enano_012:
        print(enano)
        opcion = input()
        if opcion == "1":
            sel_arma = "Martillo de Guerra"
            enano_012 = False
            final = True
        elif opcion == "2":
            sel_arma = "Trabuco"
            enano_012 = False
            final = True
        elif opcion == "3":
            enano_012 = False
            alianza_010 = True
        elif opcion == "4":
            enano_012 = False
            bando_01 = True
        elif opcion == "5":
            enano_012 = False
            flag_00 = True
        else:
            input("Porfavor pulse un numero valudo")

    while horda_020:
        print(horda)
        opcion = input()
        if opcion == "1":
            horda_020 = False
            orco = True
            sel_alianza = "Orco"
        elif opcion == "2":
            horda_020 = False
            no_muerto_022 = True
            sel_alianza = "No Muerto"
        elif opcion == "3":
            horda_020 = False
            bando_01 = True
        elif opcion == "4":
            horda_020 = False
            flag_00 = True
        else:
            input("Porfavor pulse un numero valudo")

    while orco_021:
        print(orco)
        opcion = input()
        if opcion == "1":
            sel_arma = "Maza"
            orco_021 = False
            final = True
        elif opcion == "2":
            sel_arma = "Martillo de guerra"
            orco_021 = False
            final = True
        elif opcion == "3":
            orco_021 = False
            horda_020 = True
        elif opcion == "4":
            orco_021 = False
            bando_01 = True
        elif opcion == "5":
            orco_021 = False
            flag_00 = True
        else:
            input("Porfavor pulse un numero valudo")

    while no_muerto_022:
        print(no_muerto)
        opcion = input()
        if opcion == "1":
            sel_arma = "Baston"
            no_muerto_022 = False
            final = True
        elif opcion == "2":
            sel_arma = "Espada"
            no_muerto_022 = False
            final = True
        elif opcion == "3":
            no_muerto_022 = False
            horda_020 = True
        elif opcion == "4":
            no_muerto_022 = False
            bando_01 = True
        elif opcion == "5":
            no_muerto_022 = False
            flag_00 = True
        else:
            input("Porfavor pulse un numero valudo")
    while final:
        print("Asi queda tu personaje:\nNombre = {}\nBando = {}\nRaza = {}\nArma = {}".format(nombre,sel_bando,sel_alianza,sel_arma))
        opcion = input("Tu decision es correcta?\n1)Si\n2)No\n")
        if opcion == "1":
            final = False
            flag_0 = False
        elif opcion == "2":
            final = False
            flag_00 = True
        else:
            print("Introduce una opcion valida")
print("Felizidades, asi queda configurado tu nuevo personaje:\n\nNombre = {}\nBando = {}\nRaza = {}\nArma = {}".format(nombre,sel_bando,sel_alianza,sel_arma))