import random
num_ale = random.randint(1,1000)
def funcion(n,alea,max):
    resultado = 0
    num = input('que numero cress que es?:')
    if num == alea:
        return resultado
    else:
        if int(num) < alea:
            if int(num) < n:
                print('el numero esta entre {} y {}'.format(n, max))
                resultado = 1 + funcion(n, alea, max)
            else:
                print('el numero esta entre {} y {}'.format(num,max))
                resultado = 1 + funcion(int(num), alea, max)
        if int(num) > alea:
            if int(num) > max:
                print('el numero esta entre {} y {}'.format(n, max))
                resultado = 1 + funcion(n, alea, max)
            else:
                print('el numero esta entre {} y {}'.format(n, num))
                resultado = 1 + funcion(n, alea, int(num))
        return resultado
print('el numero esta entre 1 y 1000')
print('CORRECTE. Has endevinat el número en el '+ str(funcion(1,num_ale,1000)) +' intent.')