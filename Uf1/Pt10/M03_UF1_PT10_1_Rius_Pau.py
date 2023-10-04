import random
while True:
    dado1 = 0
    dado2 = 0
    x = input("Quieres tirar los dados? S/N ")
    if (x == "S") or (x == "s"):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        print("Ha salido {} y {}".format(dado1,dado2))
    else:
        break