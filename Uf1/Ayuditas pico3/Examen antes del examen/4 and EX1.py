import random
jugador = 0
bot = 0
tirada = 0
while True:
    while True:
        nombre = input("Introduce tu nombre jugador: ")
        if nombre.isdigit() == True:
            print("Introduce un nombre")
        else:
            break
    print("Hola {}".format(nombre))
    while (jugador < 10000) and (bot < 10000):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        if tirada == 0:
            input("Presiona para ver la tirada del BOOT")
        elif tirada ==1:
            input("Presiona para ver tu tirada")
        print ("Dado1 = {}, Dado2 = {} y Dado3 = {}".format(d1,d2,d3))
        if d1 ==1 and d2 ==1 and d3 ==1:
            if tirada == 0:
                bot += 1000
            elif tirada == 1:
                jugador += 1000
            print("Extra 1000 puntos por tres dados uno")
        elif d1 == 1 and d2 ==1 or d1 ==1 and d3==1 or d2 ==1 and d3==1:
            if tirada == 0:
                bot += 100
            elif tirada == 1:
                jugador += 100
            print("Extra 100 puntos por dos dados uno")
        elif d1 == d2 == d3:
            if tirada == 0:
                bot += ((d1*3)*100)
            elif tirada == 1:
                jugador += ((d1*3)*100)
            print("La tirada vale {}".format(((d1*3)*100)))
        if d1 == 5:
            if tirada == 0:
                bot += 50
            elif tirada == 1:
                jugador += 50
            print("Extra de 50 puntos")
        if d2 == 5:
            if tirada == 0:
                bot += 50
            elif tirada == 1:
                jugador += 50
            print("Extra de 50 puntos")
        if d3 == 5:
            if tirada == 0:
                bot += 50
            elif tirada == 1:
                jugador += 50
            print("Extra de 50 puntos")
        print("Jugador tiene {} puntos y el bot tiene {} puntos.".format(jugador,bot))
        if tirada == 0:
            tirada = 1
        elif tirada == 1:
            tirada = 0

    respuesta = input("Quieres volver a jugar? S = Si, cualquier tecla = No")
    if respuesta == "S":
        input("Pulsa cualquier tecla para continuar")
    else:
        break
