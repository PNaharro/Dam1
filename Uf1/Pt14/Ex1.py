listaAlumnos = []
listaNotas = []
notas = ["Suspendido", "Aprovado", "Bien", "Notable", "Excelente"]
for i in range(8):
    while True:
        alumno = input("Escribe el nombre del alumno: ")
        if alumno.isalpha() == False:
            print("Escribe bien el nombre.")
        elif alumno.istitle() == False:
            print("Escribe el nombre con mayusculas")
        else:
            print("Nombre añadido...")
            listaAlumnos.append(alumno)
            break
    while True:
        nota = input("Escribe la nota del alumno: ")
        if nota.isalpha() == True:
            print("Escribe un valor valido.")
        elif nota.isdigit() == False:
            print("Coloca un valor valido")
        else:
            nota = float(nota)
            if nota > 10 or nota < 0:
                print("Pon un numero mayoro igual a 0 y menor o igual a 10. ")
            else:
                print("Nota añadida...")
                listaNotas.append(nota)
                break
input()
x = 0
y = 0
for j in listaNotas:
    if j < 5:
        x = 0
    elif j >=5 and j<6:
        x = 1
    elif j >=6 and j < 7:
        x = 2
    elif j >= 7 and j < 9:
        x = 3
    elif j >=9 and j<=10:
        x = 4
    print("{} ha obtenido un {}".format(listaAlumnos[y],notas[x]))
    y += 1