x = input("Dime una frase: ")
dicc = {}

cadena = ""
for i in x:
    if i.isalnum():
        cadena += i
    if i.isspace():
        dicc[cadena]=len(cadena)
        cadena = ""
dicc[cadena]=len(cadena)
print(dicc)