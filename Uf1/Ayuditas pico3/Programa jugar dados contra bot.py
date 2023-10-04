import random
while True:
    nombre = input("Dime tu nombre: ")
    print("Hola ", nombre ," vas a jugar contra el bot.")

    dado1 = 0
    dado2 = 0
    puntuacion1 = 0
    puntuacion2 = 0
    tirada1 = 0
    tirada2 = 0

    while (puntuacion1 < 10 and puntuacion2 < 10):

        #Tirada jugador
        print("Tirada de ",nombre)
        dado1 = random.randrange(1,7)
        print("Ha salido", dado1)
        dado2 = random.randrange(1,7)
        print("Ha salido ",dado2)
        tirada1 = dado1 + dado2
        print("Tirada de ", nombre," = ",tirada1)

        input("Pulsa cualquier tecla para continuar ")

        #Tirada bot
        print("Tirada del bot")
        dado1 = random.randrange(1, 7)
        print("Ha salido", dado1)
        dado2 = random.randrange(1, 7)
        print("Ha salido ", dado2)
        tirada2 = dado1 + dado2
        print("Tirada del bot = ", tirada2)

        #Ver a cual sumar punto
        if tirada1 > tirada2:
            puntuacion1 += 1
        elif tirada1 == tirada2:
            print("Empate, no suma para nadie")
        elif tirada2 > tirada1:
            puntuacion2 += 1
        print("Vais ",puntuacion1, " a ",puntuacion2)
        input("Pulsa cualquier tecla para continuar ")

    #Ver quien ha ganado
    if puntuacion2 < puntuacion1:
        print("Felizidades ",nombre, " has ganado")
    else:
        print("Mala suerte ",nombre," has perdido")

    resp = input("\n\n\nQuieres volver a jugarS/N")
    if resp == "S":
        input()
    else:
        break