def traspas(año1, año2):
    suma = 0
    diferencia = año2 - año1
    añox = año1
    while año1 < año2:
        if not año1%4 and (año1%100 or not año1%400):
            suma += 1
        año1 += 1
    print("De {} a {} hay {} años, {} de ellos son bisiestos.".format(añox,año2,diferencia,suma))
x = int(input("Dime un año: "))
y = int(input("Dime un año superior a {}: ".format(x)))
traspas(x,y)