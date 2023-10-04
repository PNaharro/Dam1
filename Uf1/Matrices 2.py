import random
n = 3
lista = []

for i in range(n):
    lista.append([])
    #print("************")
    for j in range(n):
        lista[i].append(random.randint(-5,20))
        #print("i,j = ",i,j)

print(lista)
print("Matriz sin ordenar")
#imprime formato chulo
for i in range(n):
    print()
    for j in range(n):
        print(str(lista[i][j]).ljust(5),end="")

print()
print("********************")

for i in range(n):
    print(lista[i][len(lista)-1-i])
    #print("i , len(lista)-1-i = ",i,len(lista)-1-i)

print("Burbuja ... ")
for pasada in range(n-1):
    for comparaciones in range(len(lista)-1-pasada):
        #lista[comparaciones] < lista[comparaciones+1]
        #print("comparaciones = ",comparaciones)
        #print("len(lista) - 1 - comparaciones = ",len(lista) - 1 - comparaciones+1)
        if lista[comparaciones][len(lista) - 1 - comparaciones] > lista[comparaciones+1][len(lista) - 1 - (comparaciones+1)]:

            lista[comparaciones][len(lista) - 1 - comparaciones] , \
            lista[comparaciones + 1][len(lista) - 1 - (comparaciones + 1)] = \
                lista[comparaciones+1][len(lista) - 1 - (comparaciones+1)] \
                , lista[comparaciones][len(lista) - 1 - comparaciones]
print("Diagonal inversa ordenada")
#imprime formato chulo
for i in range(n):
    print()
    for j in range(n):
        print(str(lista[i][j]).ljust(5),end="")

print()