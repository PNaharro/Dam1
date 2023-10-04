def comp():
    dic = []
    f = open('si.txt','r')
    for linea in f:
        linea = linea.replace(' ','')
        dni = linea[linea.find('dni')].split('!')[0].split(':')[1]
        dic[dni] = {}
        lista_datos = linea.split('!')
        for camp in lista_datos:
            if camp.find('dni') == -1:
                if camp.find('puntuaciones') !=-1:
                    dic[dni]['puntuaciones'] = camp.split(':')[1].split(',')
                else:
                    dic[dni]['puntuaciones'] = camp.split(':')[1]






comp()