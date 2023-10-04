while True:
    print("CALCULADORA")
    print("Menu Principal")
    print("1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n0 - Salir")
    print("")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        x = int(input("Dime un numero: "))
        y = int(input("Dime un numero: "))
        print("El resultado de la suma es ",x + y)
        input()
    if opcion == 2:
        x = int(input("Dime un numero: "))
        y = int(input("Dime un numero: "))
        print("El resultado de la resta es ", x - y)
        input()
    if opcion == 3:
        x = int(input("Dime un numero: "))
        y = int(input("Dime un numero: "))
        print("El resultado de la multiplicacion es ", x * y)
        input()
    if opcion == 4:
        x = int(input("Dime un numero: "))
        y = int(input("Dime un numero: "))
        if y == 0:
            print("Error, coloca un numero que no sea 0.")
            input()
        else:
            print("El resultado de la division es ", x / y)
            input()
    if opcion == 0:
        break
