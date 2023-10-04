f = open("Doc.txt")

x = f.read()

f = open("Doc2.txt", "w")
f.write(x)