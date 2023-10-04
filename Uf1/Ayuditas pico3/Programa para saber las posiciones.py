alto = 6
ancho = 6
for i in range(alto):
    for j in range(ancho):
        print("( i = {}, j = {} )".format(i,j).ljust(7),end="")
    print()