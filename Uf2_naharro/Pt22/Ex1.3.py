def ex3():
    lista=[]
    max = 0
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
            if i > max:
                max = i
        print("El numero maximo es",max)
ex3()