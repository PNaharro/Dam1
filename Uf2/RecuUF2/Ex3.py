def lucas(entrada):
    if entrada == 0:
        return 2
    elif entrada == 1:
        return 1
    return lucas(entrada - 2)+lucas(entrada - 1)
print(lucas(7))

