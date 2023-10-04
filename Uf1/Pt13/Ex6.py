lista =[]

nombre = input("Dime tu nombre: ")
lista.append(nombre)
inicial = nombre[0]+"."
lista.append(inicial)
apellido = input("Dime tu apellido: ")
lista.append(apellido)
x = "Nombre: "+lista[0]+"\nInicial: "+lista[1]+"\nApellido: "+lista[2]
print(x)