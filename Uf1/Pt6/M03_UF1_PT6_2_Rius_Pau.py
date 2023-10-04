while True:
    multiplo = int(input("Dame un numero multiplo de 10: "))
    x = multiplo
    y = 0
    if multiplo%10 == 0:
        break
    else:
        print("Dije un numero multiplo de 10")
        input()
while multiplo%10 == 0:
    if multiplo%10 == 0:
        multiplo = multiplo//10
        y = y+1
    else:
        break

print("Entrada".ljust(20),"Mensage de salida")
print(x,"".ljust(10),multiplo," por 10 elevado a", y)