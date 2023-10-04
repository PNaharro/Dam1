print("Dime las horas que has trabajado esta semana y tu pago por hora y te dire cuato cobras.")
horas = int(input("Pon aqui las horas: "))
pago = int(input("Pon aqui el pago: "))
if horas <= 35:
    print("Cobras ",horas*pago)
elif horas > 35:
    horasx = horas - 35
    horas = horas - horasx
    print("Cobraras por horas normales ",horas*pago)
    print("Cobraras por horas extra ",pago*0.5)