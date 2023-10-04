f = open('jose.txt', 'r')
a = f.read(10)
f2 = open('ar2.txt', 'w')
while len(a)>0:
    f2.write(a)
    a=f.read(10)