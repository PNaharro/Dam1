def funcionA(a,b):
    print("LA division entre a y b es: ",a/b)
    #ZeroDivisionError: division by zero

def funcionB(cadena):
    assert cadena != "casa" , "No se puede poner casa"
    print(cadena)

#funcionA(4,0)
def funcionC(a,b):
    try:
        opcion = int(input("Dame una opcion numerica: "))
        print("a")
        assert a > 0, "A no puede ser negativo"
        print("LA division entre a y b es: ", a / b)
        print("b")
    except ZeroDivisionError:
        print("Estas intentando dividir entre 0")
    except AssertionError:
        print("Me estas pasando un dividendo negativo")
    except ValueError:
        print("Introduce digitos")

#funcionB("casa")
#funcionC(2,1)
#print("Texto de ejemplo jajajajajajajajjajajajajajajajajajajjaj")

def funcionD(iterable):
    try:
        if type(iterable) not in (list, dict, str, tuple):
            raise TypeError ("No me esas pasando un elemento iterable")
        for i in iterable:
            print(i)
    except TypeError:
        print("Deberias pasar un elemento iterable")
    finally:
        print("Esto se ejecutara si o si")
funcionD(6)
