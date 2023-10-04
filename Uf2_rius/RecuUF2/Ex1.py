def funcion(base, altura):
    if altura == 1:
        return "*" * base
    print("*" * base)
    return funcion(base,altura - 1)
print(funcion(5,10))