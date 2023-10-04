
# a,b = 13,0

def suma(a,b):
    a = a+b
    return a

def resta(a,b):
    b = a-b
    return b

def multiplicar(a,b):
    c = a*b
    return c

def dividir(a,b):
    try:
        d = a / b
        return d
    except ZeroDivisionError:
        print("No pot ser una divisio entre 0")

###############################################
# Exercici 2 c
# print ('operands =', a, b)
# print ('sumar =', suma (a, b))
# print ('restar =', resta (a, b))
# print ('multiplicar =', multiplicar (a, b))
# print ('dividir =', dividir (a, b))