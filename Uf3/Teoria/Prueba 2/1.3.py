def escribir():
    nom = input("Dime tu nombre: ") + "\n"
    cognoms = input("Dime tus aprellidos: ") + "\n"
    nif = input("Dime tu NIF: ") + "\n"
    edat = input("Dime tu edad: ") + "\n"
    altura = input("Dime tu altura: ") + "\n"
    lista = [nom, cognoms, nif, edat, altura]
    f = open("persones.txt", "a")
    f.writelines(lista)
    f.close()

def leer():
    f = open("persones.txt","r")
    print(f.read())
    f.close()

while True:
    print("1)Escribir\n2)Leer\n3)Salir")
    opc = input("Opcion: ")
    if opc == "1":
        escribir()
    elif opc == "2":
        leer()
    else:
        print("Saliendo...")
        break
