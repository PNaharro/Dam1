def tres_linies ():
    print("\n"*3)
def nou_linies ():
    tres_linies()
    tres_linies()
    tres_linies()
def neteja_pantalla():
    print("\n"*25)
def cadena_n_vegades(c,n):
    for i in range(n):
        print(c)
#Ocurre que se imprimen 25 linias en blanco seguidas
neteja_pantalla()
cadena_n_vegades("Valor a repetir",6)