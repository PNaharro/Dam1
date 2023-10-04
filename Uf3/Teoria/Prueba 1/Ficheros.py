
f = open("Hola.txt")
print(f.read())
f.close()

f = open("Hola.txt","w")
print(f.write("Hola"))
f.close()

f = open("Hola.txt","a")
print(f.write(" Adios"))
f.close()

f = open("Hola.txt","rb")
print(f.read())
f.close()

import os
f = open(os.path.join("Hola.txt"),"r")
print(f.read())
f.close()