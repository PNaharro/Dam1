mitad = ""
mitad_invertida = ""
total = []
def funcion(texto,x,y,total,mitad,mitad_invertida):
    if y < len(texto)+1:
        if not texto[x:y].isspace() and not texto[x:y] == ",":
            total += texto[x:y].lower()
            if y <= (len(texto)+1)/2:
                mitad += texto[x:y].lower()
            else:
                mitad_invertida = texto[x:y].lower() + mitad_invertida
        return funcion(texto,x+1,y+1,total,mitad,mitad_invertida)
    if len(total)%2 == 0:
        if mitad == mitad_invertida:
            return True
        else:
            return False
    elif len(total)%2 ==1:
        if mitad == mitad_invertida[:-1]:
            return True
        else:
            return False
print(funcion("A luna ese anula",0,1,total,mitad,mitad_invertida))