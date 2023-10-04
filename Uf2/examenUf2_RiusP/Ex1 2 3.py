censImperi={"AR1":{"name":"Claudia","region":"Roma","age":23,"sex":"O","category":"Centurion","strength":50,"life":100},
            "AD3":{"name":"Maximo","region":"Hispania","age":30,"sex":"M","category":"Soldier","strength":60,"life":100},
            "AC2":{"name":"Marco","region":"Hispania","age":28,"sex":"W","category":"Soldier","strength":70,"life":100},
            "AV6":{"name":"Julius","region":"Roma","age":35,"sex":"M","category":"Caesar","strength":60,"life":100},
            "SS5":{"name":"Augustus","region":"Hispania","age":21,"sex":"M","category":"Soldier","strength":95,"life":100},
            "WQ6":{"name":"Eugenia","region":"Hispania","age":28,"sex":"W","category":"Soldier","strength":95,"life":100},
            "JU8":{"name":"Anastacia","region":"Hispania","age":17,"sex":"O","category":"Soldier","strength":64,"life":100},
            "DF5":{"name":"Aurelia","region":"Hispania","age":20,"sex":"W","category":"People","strength":81,"life":100},
            "BR1":{"name":"Antistia","region":"Roma","age":16,"sex":"W","category":"Centurion","strength":120,"life":100},
            "KR9":{"name":"Apolonia","region":"Roma","age":25,"sex":"O","category":"Centurion","strength":101,"life":100},
            "KH7":{"name":"Acucia","region":"Roma","age":29,"sex":"W","category":"Centurion","strength":89,"life":100},
            "XH4":{"name":"Titus","region":"Roma","age":39,"sex":"O","category":"People","strength":76,"life":100},
            "KA2":{"name":"Aurelio","region":"Roma","age":15,"sex":"M","category":"People","strength":110,"life":100},
            "MJ8":{"name":"Tiberius","region":"Roma","age":22,"sex":"M","category":"People","strength":154,"life":100},
            "XH4":{"name":"Filius","region":"Roma","age":41,"sex":"O","category":"Centurion","strength":132,"life":100},
            "KA2":{"name":"Libertus","region":"Roma","age":25,"sex":"M","category":"Centurion","strength":94,"life":100},
            "MJ8":{"name":"Arcadio","region":"Roma","age":27,"sex":"M","category":"Centurion","strength":78,"life":100},
            "RM8":{"name":"Casiano","region":"Hispania","age":27,"sex":"M","category":"Soldier","strength":86,"life":100},
            "MK8":{"name":"Cecilio","region":"Hispania","age":27,"sex":"M","category":"People","strength":79,"life":100},
            "SQ8":{"name":"Prisco","region":"Roma","age":36,"sex":"M","category":"Centurion","strength":89,"life":100},
            "MR3":{"name":"Eligio","region":"Roma","age":45,"sex":"M","category":"Centurion","strength":78,"life":100},
            "FC8":{"name":"Elvio","region":"Hispania","age":63,"sex":"M","category":"Soldier","strength":86,"life":100},
            "SX8":{"name":"Honorio","region":"Hispania","age":54,"sex":"M","category":"People","strength":79,"life":100},
            "EM8":{"name":"Patricio","region":"Roma","age":51,"sex":"M","category":"People","strength":89,"life":100},}



######################Ex1##################################
def Menu(tupla,titol):
    longitud = len(titol)//2 + 50
    cadena_t = "*"*100 +"\n" + titol.rjust(int(longitud)) + "\n" + "*"*100
    while True:
        try:
            print(cadena_t)
            cadena = ""
            for i in range(len(tupla)):
                cadena += (str(i+1)+")"+tupla[i]+"\n")
            print(cadena)
            opc = input("Opcion: ")
            int(opc)
            if int(opc) < 1 or int(opc) > len(tupla):
                int("*")
            else:
                return int(opc)
        except ValueError:
            return "Valor incorrecto"
tupla = ("Opc1","Opc2","Opc3","Opc4","Opc5")
titol = "Titulo de ejemplo"
print(Menu(tupla,titol))









#####################Ex3################################
def searchPerson(nombre):
    y = 0
    cabecera = "=" * 50 + "\n" + "Name".ljust(10) + "Region".ljust(10) + "Age".ljust(5) + "Sex".ljust(
        4) + "Category".ljust(11) + "\n" + "*" * 50
    print(cabecera)
    for i in censImperi:
        if nombre.lower() in censImperi[i]["name"].lower():
            texto = str(censImperi[i]["name"]).ljust(10) + str(censImperi[i]["region"]).ljust(10) + str(censImperi[i]["age"]).ljust(5) + str(censImperi[i]["sex"]).ljust(4) + str(censImperi[i]["category"]).ljust(11)
            print(texto)
            y = 1
    if y != 1:
        print("Error. No se encontro a la persona")


nombre = input("Nombre a buscar: ")
searchPerson(nombre)