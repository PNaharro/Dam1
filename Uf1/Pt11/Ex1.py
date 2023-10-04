while True:
    x = input("Introduce tu nombre de usuario: ")
    if len(x) < 6:
        print("El nombre de usuario ha de contener al menos 6 caracteres.")
    elif len(x) > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres.")
    elif x.isalnum() == False:
        print("El nombre de usuario solo puede contener nombres y numeros.")
    else:
        print("True")
        break