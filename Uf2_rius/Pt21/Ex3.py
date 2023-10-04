def alfabetico(palabra):
    print(palabra)
    letra = ""
    x = 0
    for i in palabra:
        letra = i
        break
    for i in palabra:
        if i == letra:
            x = 1
        elif i < letra:
            x = 2
        elif i > letra:
            x = 1
        letra = i
    if x == 1:
        print("Es una palabra alfabetica")
    elif x == 2:
        print("No es una palabra alfabetica")
alfabetico("amor")