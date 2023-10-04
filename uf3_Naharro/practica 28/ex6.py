f = open('jose.txt','r')
a = f.readlines()
dicionarios ={}
for i in a:
    var = i.split(':')
    dicionarios[var[0]]=var[1].replace('\n','')
print(dicionarios)