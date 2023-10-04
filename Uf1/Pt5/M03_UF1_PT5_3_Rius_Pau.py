print("Dame tres numeros y te digo si estan ordenados o no.")
x = int(input("El primero: "))
y = int(input("El segundo: "))
z = int(input("El tercero: "))

if x < y and y < z:
    print ("Estan ordenados")
else:
    print("Estan desordenados")