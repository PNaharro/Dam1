par = open("../Ex1/parells.txt")
sen = open("../Ex1/senars.txt")
tot = open("1a100.txt","a")

listaPares = par.read().split("\n")
listaImpares = sen.read().split("\n")
for i in range(len(listaPares[:-1])):
    tot.write(listaImpares[i]+"\n")
    tot.write(listaPares[i]+"\n")