x = int(input("Dime un numero: "))
y = 1
while y <= x:
    if x%y == 0:
        print(y," es divisor de ",x)
    y = y + 1