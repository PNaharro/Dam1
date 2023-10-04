def palabra(pal,let):
    x = 1
    for i in pal:
        if i == let:
            print("La posicion en la que se encuentra la letra es ",x)
        else:
            respuesta = 1
        x += 1
pal = input("Dime una palabra: ")
let = input("Dime la letra a buscar en la palabra: ")
palabra(pal,let)