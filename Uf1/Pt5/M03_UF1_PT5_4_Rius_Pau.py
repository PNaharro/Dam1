x = int(input("Dime un año y te digo si es bisiesto o no: "))
if x%4 == 0 and x%100 == 0 and x%400 == 0:
    print("Es bisiesto")
elif x%4 == 0 and x%100 == 0:
    print("No es bisiesto")
elif x%4 == 0:
    print("Es Bisiesto")