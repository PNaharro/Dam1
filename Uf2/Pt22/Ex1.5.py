def ex5():
    lista=[]
    try:
        while True:
            x = float(input("Dime numeros: "))
            if x >= 0:
                lista.append(x)
            elif x < 0:
                break
    except:
        print("Esto no se puede añadir")
    finally:
        print("La lonjitud de la lista es",len(lista))
ex5()