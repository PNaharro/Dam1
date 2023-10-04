import random
x = random.randrange(1,101)
for i in range(5):
    y = int(input("Dime un numero del 1 al 100: "))
    if y == x:
        print("Ganaste")
        break
    else:
        if y > x:
            print("Tu numero es mayor")
        elif y < x:
            print("Tu numero es menor")
if y != x:
    print("Se te acabaron las oportinidades")