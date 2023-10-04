horas = int(input("Dime cuantas horas trabajo: "))
metros = int(input("Dime cuantos metros de cable: "))
horas_total = horas * 30
metros_total = metros * 0.5
total = horas_total + metros_total
print("El precio en bruto es ", total, " euros.")
total_iva = total*1.21
print("El precio con IVA es ", total_iva," euros.")