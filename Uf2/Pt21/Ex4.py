lista1 = [1, 2, 1,1,5]
def listas(*lista2):
    lista3 = []
    for i in lista1:
        for j in lista2:
            if i == j:
                lista3.append(i)
    print(lista3)
listas(2,3,2,4,5,0)