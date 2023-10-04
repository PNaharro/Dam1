def ex3():
    lista = []
    lista1 = []
    lista2 = []
    try:
        while True:
            x = str(input("Dime una palabra: "))
            if x == "fi" or x == "Fi":
                break
            lista.append(x)
    except:
        print("Esto no se puede introducir")
    finally:
        for i in lista:
            if i not in lista1:
                lista1.append(i)
            else:
                if i not in lista2:
                    lista2.append(i)
        print(lista2)
ex3()