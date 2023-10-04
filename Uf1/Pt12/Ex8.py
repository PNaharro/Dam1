lestrasDNI = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
dni = int(input("Dime el numero de tu dni y te digo la letra que le corresponde: "))
x = dni%23
print(dni,lestrasDNI[x],sep="")