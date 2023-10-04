n = int(input("Posa un numero major o igual a 6 (si no es igual o major a 6 no surtira el dibuix): "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n:
            print("*", end="")
        elif i == 2 or i == n - 1:
            if j == 1 or j == n:
                print("*", end="")
            else:
                print("#", end="")
        else:
            if j == 2 or j == n-1:
                print("#", end="")
            else:
                print("*", end="")
    print("")
