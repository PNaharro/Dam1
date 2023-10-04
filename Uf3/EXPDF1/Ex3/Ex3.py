personas = open("persones.txt","a")

# while True:
#     lista = []
#     nombre = input("Dime el nombre: ")
#     lista.append("nombre:"+nombre+"!")
#     apellidos = input("Dime los apellidos: ")
#     lista.append("apellidos:" + apellidos+"!")
#     nif = input("Dime el DNI: ")
#     lista.append("dni:" + nif+"!")
#     edad = input("Dime la edad: ")
#     lista.append("edad:" + edad+"\n")
#
#     personas.writelines(lista)
#
#     opc = input("Quieres añadir mas personas: S/N")
#     if opc == "N" or opc == "n":
#         break

personas2 = open("persones2.txt","a")

while True:
    lista = []
    nombre = input("Dime el nombre: ")
    lista.append("Nombre = "+nombre+"\n")
    apellidos = input("Dime los apellidos: ")
    lista.append("Apellidos = "+apellidos+"\n")
    nif = input("Dime el DNI: ")
    lista.append("DNI = " + nif + "\n")
    edad = input("Dime la edad: ")
    lista.append("Edad = " + edad+"\n")

    personas2.writelines(lista)

    opc = input("Quieres añadir mas personas: S/N")
    if opc == "N" or opc == "n":
        break
