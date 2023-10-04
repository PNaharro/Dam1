def cont():
    f = open('si.txt', 'r')
    dic= {}
    for i in f.readlines():
        var = i.split('!')
        punt = var[2].split(':')
        puntuacion = punt[1].split(',')
        dni = var[0].split(':')
        name = var[1].split(':')
        clas = var[3].split(':')
        dic[dni[1]] = {'nombre':name[1],'puntuaciones':puntuacion,'clasificacion':clas[1].replace('\n','')}
    print(dic)
    return dic
dicionario = cont()
def dent(dic):
    f=open('arc.txt','w')
    for i in dic:
        cadena = 'dni: '+str(i)+'!nombre:'+str(dic[i]['nombre'])+'!putuaciones:'+str(dic[i]['puntuaciones'])+'!clasificacion:'+str(dic[i]['clasificacion'])+'\n'
        f.write(cadena)
dent(dicionario)