tupla = ("hola",32,["a","b"],(3,2,5))

# tupla1 = (3)
# print(type(tupla1))
# tupla2 = (3,)
# print(type(tupla2))
#
# anabel = ("Anabel Lorca Suarez","55554444Y","Calle Vasubio 7 8º 4ª", "+0034633780192")
# nombre, dni, direccion, telefono = anabel
# print(nombre, dni, direccion, telefono)


#Lo logico
# var1 = 5
# var2 = 10
#
# aux = var1
# var1=var2
# var2 = aux

#Excusivo del pyton e igual de efectivo
# var1,var2=var2,var1



#Compara el primer elemento con el primero del otro
# tupla1 = (1,2,3)
# tupla2 = (4,5,6)
# print(tupla1>tupla2)

# tupla1 = (5,1,2,3)
# tupla2 = (4,5,6)
# print(tupla1 > tupla2)

# tupla1 = (1,2,3)
# tupla2 = (1,2,3,4)
# print(tupla1>tupla2)

#Esto ta bien
# tupla2 = (1,2,3,4,5,6,7)
# for i in tupla2:
#     print("i = ",i)
# for i in range(len(tupla2)):
#     print("i = ",tupla2[i])

#Conversion de tupla a lista y biceversa
tupla1 = (1,2,3)
tupla2 = (1,2,3,4)
lista = list(tupla1)
print(lista)

lista1 = ["a","b","c"]
tupla3 = tuple(lista1)
print(tupla3)
