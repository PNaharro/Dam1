dia = int(input("Dime tu dia de nacimiento: "))
mes = int(input("Dime tu mes de nacimiento: "))
año =int(input("Dime tu año de nacimiento: "))
x = int(str(dia)+str(mes)+str(año))
residuo = 0
suma = 0
while x != 0:
    residuo = x % 10
    x = x // 10
    suma = suma + residuo
residuo1 = 1
suma1 = 1
while suma >= 10:
    residuo1 = suma % 10
    suma = suma // 10
    suma1 = suma1 + residuo1
print("Tu numero de la suerte es: ",suma1)
