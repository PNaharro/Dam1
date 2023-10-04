def ex1():
    lista=[]
    try:
        while True:
            x = float(input("Dime un numero: "))
            if x >= 0:
                lista.append(x)
            elif x<0:
                break
    except:
        print("Este caracter no se puede añadir")
    finally:
        print(lista)
ex1()