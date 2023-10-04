def divisor(x):
    y = 1
    while y <= x:
        if x%y == 0:
            print(y,end=" ")
        y += 1
x = int(input("Dime un numero: "))
divisor(x)