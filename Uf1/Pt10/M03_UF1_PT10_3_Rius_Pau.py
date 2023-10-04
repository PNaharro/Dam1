import random
n = int(input("Hasta que numero quieres que genere? "))
for i in range(n):
    x = random.randrange(2,n,2)
    print(x)