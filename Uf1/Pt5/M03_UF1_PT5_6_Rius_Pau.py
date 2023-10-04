print("======================")
print("= 1.- Euros a dolares")
print("= 2.- Euros a Yenes")
print("= 3.- Dolaers a Euros")
print("= 4.- Dolares a Yenes")
print("= 5.- Yenes a Euros")
print("= 6.- Yenes a Dolares")
print("======================")
x = int(input("= Escoge una opcion ="))
print("======================")

dolar = 1.11894
yen = 115.998

if x == 1:
    euros = int(input("Dime el numero de Euros: "))
    print ("Dolars = ",euros*dolar)
elif x == 2:
    euros = int(input("Dime el numero de Euros: "))
    print ("Yenes = ",euros*yen)
elif x == 3:
    dolares = int(input("Dime el numero de Dolares: "))
    print ("Euros = ",dolares/dolar)
elif x == 4:
    dolares = int(input("Dime el numero de Dolares: "))
    y = dolares/dolar
    y = y * yen
    print("Yenes = ",y)

elif x == 5:
    yenes = int(input("Dime el numero de Yenes: "))
    print("Euros = ",yenes/yen)

elif x == 6:
    yenes = int(input("Dime el numero de Yenes: "))
    y = yenes/yen
    y = y * dolar
    print("Dolares = ",y)
