cantidad = int(input("Dime cuantos numero quieres introducir: "))
suma = 0
mayor = 0
menor = 10000000000
for i in range(cantidad):
    numero = int(input("Numero: "))
    suma = suma + numero
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
mediana = suma/cantidad

print("Has introducido {} numeros, el mayor de estos es {}, el menor es {} y la mediana es {}".format(cantidad,mayor,menor,mediana))