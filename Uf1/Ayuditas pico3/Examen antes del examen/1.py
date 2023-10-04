ancho = int(input("Introduce la anchura: "))
alto = int(input("Introduce la altura: "))
for i in range(alto):
    for j in range(ancho):
        # if (i == 1 or j == 1 or i == alto - 2 or j == ancho - 2 ):
        if (i ==0  and j==0) or (i==0 and j==ancho-1) or (i==alto-1 and j==0) or (i==alto-1 and j==ancho-1) or (i==1 and j>>0 and j<=ancho-2) or\
                (i ==alto-2 and j>=1 and j<=ancho-2) or (i >=1 and i<=alto-2 and j==1) or (i >=1 and i<=alto-2 and j==ancho-2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
