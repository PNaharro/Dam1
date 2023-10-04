x = int(input("Entrada del numero: "))
while True:
    if x%2==0:
        x//=2
    elif x%2==1:
        x*=3
        x+=1
    elif x==2:
        x-=1
    print("Sucesion generada {}".format(x))
    if x==1:
        break