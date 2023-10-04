def tablasbaratas(nomf1,nomf2,p):
    Nom_model = ''
    Nivell_velocitat = ''
    f = open(nomf1,'r')
    f1 = open(nomf2, 'w')
    var = f.readlines()
    for i in var:
        tot = i.split(';')
        Nom_model = tot[0][0:2]+'-'+tot[1]
        if int(tot[3]) < 500:
            Nivell_velocitat = 'Baja'
        elif int(tot[3]) >= 500 or int(tot[3]) <= 900:
            Nivell_velocitat = 'Mitja'
        if int(tot[3]) > 900:
            Nivell_velocitat = 'Alta'
        f1.write(Nom_model+' '+Nivell_velocitat+'\n')
tablasbaratas('nomf1','nomf2',2)