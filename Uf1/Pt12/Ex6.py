menor = "z"
for i in range(5):
    while True:
        y = input("Dime una palabra: ")
        if y.isdigit() == True:
            print("Palabras")
        else:
            break
    if y < menor:
        menor = y
    else:
        menor = menor
    print(menor)