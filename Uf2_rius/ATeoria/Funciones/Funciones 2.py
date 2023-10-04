def funcion1(par1,par2="valor por defecto"):
    print("Par 1 =",par1)
    print("Par 2 =",par2)

# funcion1("Valor 1")
# print()
# funcion1("Valor 1","Valor 2")

#Los valores por defecto, al final (da error)
# def funcion2(par2="valor por defecto",par1):
#     print("Par 1 =", par1)
#     print("Par 2 =", par2)

#Como tener varios parametros pero solo cambiar los parametros elegidos
def funcion3(par1,par2="valor por defecto2",par3="Valor por defecto3",par4="Valor por defecto4"):
    print("Par 1 =", par1)
    print("Par 2 =", par2)
    print("Par 3 =", par3)
    print("Par 4 =",par4)
# funcion3("Valor 1",par4="Valor 4",par2="Valor 2")
# print()
# funcion3("Valor 1","valor2","valor3","valor x")
#Esto da error
# funcion3("Valor1","Valor 2",par3="Valor 3","Valor 4")

#Ponemos * en el ultimo parametro para decirle que todos los valores que entren seran para ese parametro
def funcion4(nombre, *numeros):
    print("Hola",nombre)
    print(numeros)
    suma = 0
    for i in numeros:
        suma += i
    print("Suma =",suma)
# funcion4("Pepe",1,2)
# print()
# funcion4("Pepe",1,2,3)
# print()
# funcion4("Pepe",1,2,3,4)

#Cosas esta siendo un diccionario
def funcion5(nombre,*numeros,**cosas):
    print("Hola ",nombre)
    print("Numeros: ",numeros)
    print("Cosas: ",cosas)
funcion5("Pepe",1,2,3,a="Valor 1",b="Valor 2",c="Valor 3")