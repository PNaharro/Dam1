def ex6():
    lista=[]
    suma = 0
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
        for i in lista:
            suma += i
        print("La media de la lista es",suma/len(lista))
ex6()