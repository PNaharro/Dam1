f = open("persones.txt", "r")

while True:
    nombre = f.readline().replace("\n","")
    apellidos = f.readline().replace("\n","")
    nif = f.readline().replace("\n","")
    edad = f.readline().replace("\n","")
    if edad == "":
        break
    else:
        edad = int(edad)
    altura = f.readline().replace("\n","")

    if edad >= 18:
        print(nombre)
        print(apellidos)
        print(nif)
        print(edad)
        print(altura)