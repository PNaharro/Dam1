import random
def funcionA(param1):
    if param1 > 0:
        resultado = 10 + funcionA(param1-1)
    else:
        resultado = 10
    return resultado

def funcionB():
    print("soy la funcion b")
    param3 = funcionC()
    resultado = param3**2
    return resultado

def funcionC():
    print("Estoy en la funcion C")
    resultado = random.randint(1,10)
    return resultado

def funcionfactorial(n):
    if n == 0:
        resultado = 1
    else:
        resultado = n * funcionfactorial(n-1)
    return resultado

print(funcionfactorial(6))