import random
lista1 = []
lista2 = []
for x in range(random.randint(5,10)):
    lista1.append(random.randint(0,30))
    lista2.append(random.randint(0,30))
print("Lista 1 =", lista1)
print("Lista 2 =", lista2)
def superposicio():
    x = 0
    for i in lista1:
        for j in lista2:
            if i == j:
                x = 1
    if x == 1:
        print("True")
    else:
        print("False")
superposicio()