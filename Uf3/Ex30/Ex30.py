def  tabletsBarats (nomf1, nomf2, p):
    x = ""
    for i in nomf1.read():
        x += i
    print(x[:len(x)])
    print()
    print(x)

nomf1 = open("nomf1.txt")
nomf2 = open("nomf2.txt")
p = 90.00
tabletsBarats(nomf1,nomf2,p)