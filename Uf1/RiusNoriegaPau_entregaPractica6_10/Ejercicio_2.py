import random
while True:
    a = 9
    b = 9
    dado = 0
    print("Bienvenidos al juego del dado: ")
    while True:
        input("Pulsa cualquier letra para continuar ")
        dado = random.randint(1,6)
        print("Ha salido ", dado)
        if dado%2 == 0:
            print("Ha salido Par, menos {} puntos para Anna".format(dado))
            a = a - dado
            b = b + dado
            print("Vais {} a {}".format(a,b))
        elif dado%2 == 1:
            print("Ha salido Impar, menos {} puntos para Bernat".format(dado))
            b = b - dado
            a = a + dado
            print("Vais {} a {}".format(a, b))
        if a <= 0:
            print("Felicidades Bernat, has ganado")
            break
        if b <= 0:
            print("Felicidades Anna, has ganado")
            break
    x = input("Quereis volver a jugar? S/N")
    if x == "S" or x =="s":
        print("Reiniciando partida...\n\n\n")
    else:
        print("Cerrando juego...")
        break