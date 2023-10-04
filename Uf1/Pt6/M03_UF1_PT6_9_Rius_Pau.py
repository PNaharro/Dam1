x = int(input("Cuantos numeros vas a introducir: "))
contador = 0
for i in range(x):
    i = int(input("Dame el numero: "))
    if i < 0:
        contador = contador + 1
print("Has escrito ",contador," un numero negativo.")