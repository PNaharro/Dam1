lista = [ [99,4,3,-1],
[-5,4,-8,55],
[33,-1,-5,-3],
[-2, 6, 8, 5] ]

print("Desordenado")
for i in range(4):
    print()
    for j in range(4):
        print(str(lista[i][j]).ljust(5),end="")

for i in range(3):
    for j in range(len(lista)-1-i):
        if lista[j][len(lista) - 1 - j] > lista[j+1][len(lista) - 1 - (j+1)]:
            lista[j][len(lista) - 1 - j] , lista[j + 1][len(lista) - 1 - (j + 1)] = lista[j+1][len(lista) - 1 - (j+1)] \
                , lista[j][len(lista) - 1 - j]

print("\nResultado")
for i in range(4):
    print()
    for j in range(4):
        print(str(lista[i][j]).ljust(5),end="")

print()
