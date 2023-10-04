censImperi={"AR1":{"name":"Claudia","region":"Roma","age":23,"sex":"O","category":"Centurion","strength":50,"life":100},"AD3":{"name":"Maximo","region":"Hispania","age":30,"sex":"M","category":"Soldier","strength":60,"life":100},"AC2":{"name":"Marco","region":"Hispania","age":28,"sex":"W","category":"Soldier","strength":70,"life":100},"AV6":{"name":"Julius","region":"Roma","age":35,"sex":"M","category":"Caesar","strength":60,"life":100},"SS5":{"name":"Augustus","region":"Hispania","age":21,"sex":"M","category":"Soldier","strength":95,"life":100},"WQ6":{"name":"Eugenia","region":"Hispania","age":28,"sex":"W","category":"Soldier","strength":95,"life":100},"JU8":{"name":"Anastacia","region":"Hispania","age":17,"sex":"O","category":"Soldier","strength":64,"life":100},"DF5":{"name":"Aurelia","region":"Hispania","age":20,"sex":"W","category":"People","strength":81,"life":100},"BR1":{"name":"Antistia","region":"Roma","age":16,"sex":"W","category":"Centurion","strength":120,"life":100},"KR9":{"name":"Apolonia","region":"Roma","age":25,"sex":"O","category":"Centurion","strength":101,"life":100},"KH7":{"name":"Acucia","region":"Roma","age":29,"sex":"W","category":"Centurion","strength":89,"life":100},"XH4":{"name":"Titus","region":"Roma","age":39,"sex":"O","category":"People","strength":76,"life":100},"KA2":{"name":"Aurelio","region":"Roma","age":15,"sex":"M","category":"People","strength":110,"life":100},"MJ8":{"name":"Tiberius","region":"Roma","age":22,"sex":"M","category":"People","strength":154,"life":100},"XH4":{"name":"Filius","region":"Roma","age":41,"sex":"O","category":"Centurion","strength":132,"life":100},"KA2":{"name":"Libertus","region":"Roma","age":25,"sex":"M","category":"Centurion","strength":94,"life":100},"MJ8":{"name":"Arcadio","region":"Roma","age":27,"sex":"M","category":"Centurion","strength":78,"life":100},"RM8":{"name":"Casiano","region":"Hispania","age":27,"sex":"M","category":"Soldier","strength":86,"life":100},"MK8":{"name":"Cecilio","region":"Hispania","age":27,"sex":"M","category":"People","strength":79,"life":100},"SQ8":{"name":"Prisco","region":"Roma","age":36,"sex":"M","category":"Centurion","strength":89,"life":100},"MR3":{"name":"Eligio","region":"Roma","age":45,"sex":"M","category":"Centurion","strength":78,"life":100},"FC8":{"name":"Elvio","region":"Hispania","age":63,"sex":"M","category":"Soldier","strength":86,"life":100},"SX8":{"name":"Honorio","region":"Hispania","age":54,"sex":"M","category":"People","strength":79,"life":100},"EM8":{"name":"Patricio","region":"Roma","age":51,"sex":"M","category":"People","strength":89,"life":100},}

categoria = ["Centurion","Soldier","Caesar","People"]

#Ex1
def setProperty(opc):
    if opc in categoria:
        return opc
    else:
        return False
def showCategory():
    while True:
        opc = input("Dime la categoria: ")
        x = setProperty(opc)
        if x == False:
            print("Escribe la categoria bien")
        else:
            break
    lista_x =[]
    for i in censImperi:
        if censImperi[i]["category"] == x:
            lista_x.append(i)
    for i in censImperi:
        if censImperi[i]["category"] == x:
            print("Nombre:",censImperi[i]["name"])
            print("Region:",censImperi[i]["region"])
            print("Edad:",censImperi[i]["age"])
            print("Sexo:",censImperi[i]["sex"])
            print("Categoria:",censImperi[i]["category"])
            print("Total:",len(lista_x))
            input("Presiona para continuar")
showCategory()

#Ex2
import random

ej_roma = {}
ej_hispania = {}
lista_ej_roma = []
lista_ej_hispania = []
def setArmies():
    for i in censImperi:
        if censImperi[i]["category"] == "Centurion" and censImperi[i]["region"] == "Roma":
            lista_ej_roma.append(i)
        if censImperi[i]["category"] == "Soldier" and censImperi[i]["region"] == "Hispania":
            lista_ej_hispania.append(i)
    while True:
        r1 = random.randint(0,len(lista_ej_roma)-1)
        r2 = random.randint(0,len(lista_ej_roma)-1)
        if r1 != r2:
            while True:
                r3 = random.randint(0,len(lista_ej_roma)-1)
                if r3 != r1 and r3 != r2:
                    break
        break
    ej_roma[lista_ej_roma[r1]] = lista_ej_roma[r1]
    ej_roma[lista_ej_roma[r2]] = lista_ej_roma[r2]
    ej_roma[lista_ej_roma[r3]] = lista_ej_roma[r3]
    while True:
        r1 = random.randint(0,len(lista_ej_hispania)-1)
        r2 = random.randint(0,len(lista_ej_hispania)-1)
        if r1 != r2:
            while True:
                r3 = random.randint(0,len(lista_ej_hispania)-1)
                if r3 != r1 and r3 != r2:
                    break
        break
    ej_hispania[lista_ej_hispania[r1]] = lista_ej_hispania[r1]
    ej_hispania[lista_ej_hispania[r2]] = lista_ej_hispania[r2]
    ej_hispania[lista_ej_hispania[r3]] = lista_ej_hispania[r3]
    print("Army Hispania".center(60,"=") + "\n" + "name".ljust(15) + "region".ljust(15) + "age".ljust(5) + "sex".ljust(10) + "strength".ljust(10) + "life" +
          "\n" + "*"*60)
    for i in ej_hispania:
        cadena = censImperi[i]["name"].ljust(15) + censImperi[i]["region"].ljust(15) + str(censImperi[i]["age"]).ljust(5) + censImperi[i]["sex"].ljust(10) + \
                 str(censImperi[i]["strength"]).ljust(10) + str(censImperi[i]["life"])
        print(cadena)
    print()
    print("Army Roma".center(60, "=") + "\n" + "name".ljust(15) + "region".ljust(15) + "age".ljust(5) + "sex".ljust(
        10) + "strength".ljust(10) + "life" +
          "\n" + "*" * 60)
    for i in ej_roma:
        cadena = censImperi[i]["name"].ljust(15) + censImperi[i]["region"].ljust(15) + str(censImperi[i]["age"]).ljust(5) + censImperi[i]["sex"].ljust(10) + \
                 str(censImperi[i]["strength"]).ljust(10) + str(censImperi[i]["life"])
        print(cadena)
    armies = (ej_roma,ej_hispania)
    return armies
setArmies()


#Ex4
def showArmy(region="Hispania"):
    try:
        if region != "Roma" and region != "Hispania":
            int("*")
        else:
            if region == "Roma":
                lista_roma = []
                lista_roma_e = []
                for i in censImperi:
                    if censImperi[i]["region"] == "Roma" and censImperi[i]["category"] == "Centurion":
                        lista_roma.append(i)
                        lista_roma_e.append(censImperi[i]["age"])
                for i in range(len(lista_roma_e) - 1):
                    for j in range(len(lista_roma_e) - i - 1):
                        if lista_roma_e[j] < lista_roma_e[j + 1]:
                            numero = lista_roma_e[j]
                            lista_roma_e[j] = lista_roma_e[j + 1]
                            lista_roma_e[j + 1] = numero

                            numero = lista_roma[j]
                            lista_roma[j] = lista_roma[j + 1]
                            lista_roma[j + 1] = numero
                print("Centurions from Roma".center(73) + "\n" + "*"*73 + "\n" + "Name".ljust(15) + "Region".ljust(15) + "Age".ljust(10) + "Sex".ljust(10) +
                      "Category".ljust(15) + "Strength" + "\n" + "*"*73)
                for i in lista_roma:
                    cadena = censImperi[i]["name"].ljust(15) + censImperi[i]["region"].ljust(15) + str(censImperi[i]["age"]).ljust(10) + censImperi[i]["sex"].ljust(10) +\
                             censImperi[i]["category"].ljust(15) + str(censImperi[i]["strength"])
                    print(cadena)
            else:
                lista_hispania = []
                lista_hispania_e = []
                for i in censImperi:
                    if censImperi[i]["region"] == "Hispania" and censImperi[i]["category"] == "Soldier":
                        lista_hispania.append(i)
                        lista_hispania_e.append(censImperi[i]["age"])
                for i in range(len(lista_hispania_e) - 1):
                    for j in range(len(lista_hispania_e) - i - 1):
                        if lista_hispania_e[j] < lista_hispania_e[j + 1]:
                            numero = lista_hispania_e[j]
                            lista_hispania_e[j] = lista_hispania_e[j + 1]
                            lista_hispania_e[j + 1] = numero

                            numero = lista_hispania[j]
                            lista_hispania[j] = lista_hispania[j + 1]
                            lista_hispania[j + 1] = numero
                print("Soldiers from Roma".center(73) + "\n" + "*" * 73 + "\n" + "Name".ljust(15) + "Region".ljust(
                    15) + "Age".ljust(10) + "Sex".ljust(10) +
                      "Category".ljust(15) + "Strength" + "\n" + "*" * 73)
                for i in lista_hispania:
                    cadena = censImperi[i]["name"].ljust(15) + censImperi[i]["region"].ljust(15) + str(
                        censImperi[i]["age"]).ljust(10) + censImperi[i]["sex"].ljust(10) + \
                             censImperi[i]["category"].ljust(15) + str(censImperi[i]["strength"])
                    print(cadena)
    except ValueError:
        print("Introduce un valor valido")
showArmy("Roma")