print("Indica un numero: ")
h = int(input())
cont = h
dibujo = 1
for n in range(1, h):
    print(cont*str(' ')+dibujo*str('*'))
    dibujo = dibujo + 2
    cont = cont - 1
