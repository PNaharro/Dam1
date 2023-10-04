def ex4():
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
        for i in lista:
            min = i
            break
        for i in lista:
            if i < min:
                min = i
        print("El numero minimo es",min)
ex4()