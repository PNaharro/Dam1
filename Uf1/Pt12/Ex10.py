cadena = "H"+" que pAsA"+" hOla"
mayusculas = 0
x = 0
for i in range(len(cadena)):
    if cadena[x].isupper() == True:
        mayusculas +=1
    else:
        mayusculas = mayusculas
    x += 1
print("Hay",mayusculas," mayusculas")