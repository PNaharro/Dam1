alto = 6
ancho = 6
for i in range(alto):
    for j in range(ancho):
        if (i == 0 or j == 0 or i == alto - 1 or j == ancho - 1 or i >=2 and j >=2 and i <=3 and j <=3):
            print("*",end="")
        else:
            print("#",end="")
    print()