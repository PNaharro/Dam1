import math
#TRIANGULO
print("Dame la base y altura de un rectangulo y yo te calculo el perimetro y el area.")

base_triangulo = int(input("Pon aqui la base: "))
altura_triangulo = int(input("Pon aqui la altura: "))

perimetro_triangulo = 2 * base_triangulo + 2 * altura_triangulo
area_triangulo = base_triangulo * altura_triangulo
print("El perimetro es {} y el area es {}.".format(perimetro_triangulo, area_triangulo))

#CIRCULO
print("Ahora calculare el perimetro i area de un circulo, dame su radio.")
radio_circulo = int(input("Pon aqui el radio: "))

area_circulo = math.pi*radio_circulo**2
perimetro_circulo = 2*math.pi*radio_circulo
print("El area es {} y el perimetro es {}.".format(area_circulo,perimetro_circulo))

#ESFERA
print("Por ultimo te calculare el volumen de una esfera con el radio.")
radio_esfera = int(input("Pon aqui el radio: "))

volumen_esfera = (4/3)*math.pi*(radio_esfera**3)
print("El volumen es {}.".format(volumen_esfera))