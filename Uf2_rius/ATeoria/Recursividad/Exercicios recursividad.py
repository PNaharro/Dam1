# x = int(input("Dime un numero y te hago el factorial: "))
#
# y = x
# for i in range(x):
#     y -=1
#     if y == 0:
#         break
#     x *= y
# print("El factorial es =",x)


# def funcion(i):
#    if i != 10:
#        print("I = ",i)
#        funcion(i + 1)
#     if i == 10:
#         print("I = ", i)
#        return
# funcion(1)

#10 = n
# for i in range(10):
#     for j in range(10):
#         print("(i,j)",i,j)


# def forAnidadoRecursivo(n,m,i,j):
#     if i == n and j == m:
#         return
#     elif j == m:
#         forAnidadoRecursivo(n,m,i+1,0)
#     else:
#         print("(i, j)",i,j)
#         forAnidadoRecursivo(n,m,i,j+1)
#
# forAnidadoRecursivo(6,8,0,0)

#De 0 a n
# def funcion(n):
#     if n!=0:
#         funcion(n-1)
#     if n>=0:
#         print("N =",n)
#         return
# n = int(input("Numero: "))
# funcion(n)


def funcion(n):
    if n != 0:
        funcion(n-1)
    if n >= 0:
        cadena = "N = " + str(n)
        print(cadena)
        return

n = int(input("Numero: "))
funcion(n)



#Hecho
# def funcion(i):
#     if i < 15:
#         print("I = ", i)
#         funcion(i + 1)
#     else:
#         print("I = ", i)
#         return
# funcion(1)