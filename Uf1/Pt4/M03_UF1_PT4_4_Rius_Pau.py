print("Dime una cantidad de dinero, el porcentaje de inereses y los años, y te calcula cuanto pagaras.")
C = int(input("Dime la cantidad de dinero: "))
x = int(input("Dime la cantidad de inetes: "))
n = int(input("Dime la cantidad de años: "))

Cn = C * (1 + x/100) ** n
print("La cantidad a pagar es: {}".format(Cn))