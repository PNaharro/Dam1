while True:
    x = input("Introduce tu contraseña: ")
    if len(x)<8:
        print("La contraseña escogida no es segura.")
    elif x.isalnum()==False:
        print("La contraseña escogida no es segura.")
    elif x.isalpha() == True:
        print("La contraseña escogida no es segura.")
    elif x.isdigit()==True:
        print("La contraseña escogida no es segura.")
    elif x.isspace()==True:
        print("COntiene espacios")
    elif x.islower()==True:
        print("La contraseña escogida no es segura.")
    elif x.isupper()==True:
        print("La contraseña escogida no es segura.")
    else:
        print("True")
        break
