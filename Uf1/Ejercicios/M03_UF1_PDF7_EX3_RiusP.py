import random
while True:
    x = random.randrange(1,4)
    y = int(input("Elije 1.piedra, 2.papel o 3.tijera: "))
    if x == y:
        print(x)
        print("Empate")
    elif (y == 1 and x == 2) or (y == 2 and x == 3) or (y == 3 and x == 1):
        print(x)
        print("Has perdido")
        break
    else:
        print(x)
        print("Has ganado")
        break