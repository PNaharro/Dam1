def dinero(dinero):
    x = 500
    y = 0
    lista_billetes = [500,200,100,50,20,10,5,2,1]
    dicc_billetes = {500:0,200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
    while y != 8:
        if dinero/x>=1:
            dicc_billetes[x] += 1
            dinero -= x
        else:
            y += 1
            x = lista_billetes[y]
    print(dicc_billetes)

dinero(434)