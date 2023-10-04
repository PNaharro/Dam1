archivo = input('escribe nombre del archivo: ')
N_archivo = archivo+'.txt'
N = input('escribe un numero: ')
f = open(N_archivo,'r')
lineas = f.readlines()
for linea in range(int(N)):
    print(lineas[linea])
