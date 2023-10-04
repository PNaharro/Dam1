f = open("Doc.txt")
n = int(input("Dime el numero donde quieres que pare: "))
for i in list(f)[:n]:
    print(i,end="")
