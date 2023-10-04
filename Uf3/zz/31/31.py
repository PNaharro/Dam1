f=open("Doc.txt")
# for i in list(f):
#     print(i)

x = f.read()
print(x)
print(type(x))
lista = []
for i in x:
    lista.append(i)
print(lista)