import Funciones as Fun


textOpts = "\n1)Jugar\n2)Crear\n3)Editar\n4)Listar\n5)Salir"
inputOptText = "\nElige tu opcion: "
rangeList = [1,2,3,4,5]
exceptions = []
while True:
    opc = Fun.getOpt_menuprincipal(textOpts,inputOptText,rangeList,exceptions)
    if opc == 1:
        print("Jugar")
    elif opc == 2:
        print("Crear")
    elif opc == 3:
        print("Editar")
    elif opc == 4:
        print("Listar")
    elif opc == 5:
        print("Saliendo...")
        break