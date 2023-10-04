def comp():
    dic ={}
    c = open('Cara.txt','r')
    d = open('Dura.txt ','r')
    lineas_C = c.readlines()
    lineas_D = d.readlines()

    for i in range(len(lineas_C)):
        dic[i]={'codigo':lineas_C[i][0:6],'nombre':lineas_C[i][6:37],'calle':lineas_C[i][37:68],'pais':lineas_C[i][68:].replace('\n','')}
    for i in range(len(lineas_D)):
        dic[len(dic)+1]={'codigo':lineas_D[i][0:6],'nombre':lineas_D[i][6:37],'calle':lineas_D[i][37:68],'pais':lineas_D[i][68:].replace('\n','')}
    dics = list(dic.keys())
    for pasadas in range(len(dic) - 1):
        for comp in range(len(dic) - 1 - pasadas):
            if dic[dics[comp]]['nombre'] > dic[dics[comp + 1]]['nombre']:
                dics[comp], dics[comp + 1] = dics[comp + 1], dics[comp]
    f = open('clientes.txt','w')
    for i in dics:
        cadena = dic[i]['codigo']+dic[i]['nombre']+dic[i]['calle']+dic[i]['pais']
        f.write(cadena+'\n')
comp()