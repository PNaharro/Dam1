def fibonnacci(n):
    resultado = 0
    if n == 0:
        return resultado
    elif n == 1:
        resultado = 1
        return resultado
    else:
        resultado = fibonnacci(n-1)+fibonnacci(n-2)
        return resultado

for i in range(10):
    print("fibonnacci{}".format(i),fibonnacci(i))