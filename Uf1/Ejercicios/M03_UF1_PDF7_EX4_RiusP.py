import random
ganadas = 0
perdidas = 0
while True:
    a = random.randrange(11)
    b = random.randrange(11)
    j = input("Apuestas por A o por B? ")
    if (j == "A") or (j == "a"):
        if a > b:
            print("A es ", a, " y B es ", b)
            print("Has ganado!")
            ganadas +=1
            print("Has ganado ",ganadas," veces y has perdido ",perdidas," veces.")
        else:
            print("A es ", a, " y B es ", b)
            print("Has perdido")
            perdidas +=1
            print("Has ganado ",ganadas," veces y has perdido ",perdidas," veces.")
    elif (j == "B") or (j == "b"):
        if b > a:
            print("A es ", a, " y B es ", b)
            print("Has ganado!")
            ganadas +=1
            print("Has ganado ",ganadas," veces y has perdido ",perdidas," veces.")
        else:
            print("A es ",a," y B es ",b)
            print("Has perdido")
            perdidas +=1
            print("Has ganado ",ganadas," veces y has perdido ",perdidas," veces.")
    x = input("Quieres volver a jugar? S/N: ")
    if (x == "S") or (x == "s"):
        print("")
    else:
        break