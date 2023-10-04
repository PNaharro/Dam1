par = open("../Ex1/parells.txt")
sen = open("../Ex1/senars.txt")
fichero = open("fichero.txt","a")

listaPares = par.read().split("\n")
listaImpares = sen.read().split("\n")

for i in range(len(listaPares[:-1])):
    fichero.write(listaPares[i]+"#"+listaImpares[i]+"#")