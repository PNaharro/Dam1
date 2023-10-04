f = open('jose.txt','r')
variable = f.readlines()
Nlineas = len(variable)
palabras = 0
letras = 0
for campo in variable:
    palabras += len(campo.split(' '))
    letras += len(campo.replace('\n',''))

print(Nlineas,palabras,letras)
