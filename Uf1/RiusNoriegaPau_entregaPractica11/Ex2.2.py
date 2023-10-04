while True:
    mayusculas = 0
    minuscula = 0
    espacios = 0
    numeros = 0
    password = input("Introduce la contraseña \n")

    if len(password)<8:
        print("La contraseña no es correcta, faltan caracteres")
    if password.isalnum():
        print("Le faltan caracteres especiales")
    for char in password:
        if char.isdigit():
            numeros += 1
        if char.islower():
            minuscula += 1
        if char.isupper():
            mayusculas += 1
        if char.isspace():
            espacios += 1
    if numeros == 0:
        print("No contiene numeros")
    if espacios > 0:
        print("No puede contener espacios")
    if mayusculas == 0:
        print("No tiene mayusculas")
    if minuscula == 0:
        print("No contiene minusculas")
    elif numeros > 0 and espacios == 0 and mayusculas > 0 and minuscula > 0 and password.isalpha()==False:
        print("Esta bien")
        break