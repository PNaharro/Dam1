def funcion(base, altura):
    x = "*" * base
    if altura == 1:
        return x
    print(x)
    return funcion(base,altura-1)
print(funcion(9,6))