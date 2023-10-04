while True:
    cantidad = int(input("Dime cuantos numero quieres insertar: "))
    if cantidad <= 0:
        print("Un numero mayor a 0")
    else:
        break
numero = int(input("Introduce un numero: "))
for i in range(cantidad):
    while True:
        numero = int(input("Introduce un numero diferente de {}: ".format(numero)))
        if numero == numero:
            print("Un numero diferente a {}".format(numero))
        else:
            input()