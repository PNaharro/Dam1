lista=[1,2,3,4,5,6,7,8,9]
x=0
suma = 0
for i in lista:
    suma = suma + lista[x]
    x+=1
print("La suma de la lista es {}".format(suma))
y = 0
f=1
for i in lista:
    f = f * lista[y]
    y+=1
    print("El factorial de la lista es,",f)