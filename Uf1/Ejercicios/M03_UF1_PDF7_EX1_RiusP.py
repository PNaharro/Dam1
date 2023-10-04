import random
while True:
    x = random.randrange(1,11)
    y = int(input("Dime un numero: "))
    if y == x:
        print(x)
        print("Has ganado")
        break
    else:
        print(x)
        print("Fallaste, repite")