tipus={
 1:{'tipus':"Tipus1","subtipus":'Planta',"Moviment":"Normal",'categoria':'Categoria0' },
 2:{'tipus':"Tipus2","subtipus":'Veri',"Moviment":'Fisic','categoria':'Categoria0'},
 3:{'tipus':"Tipus2","subtipus":'Veri',"Moviment":'Especial','categoria':'Platino'},
 4:{'tipus':"Tipus2", "subtipus":'Veri', "Moviment": 'Especial', 'categoria': 'Rubi'},
 5:{'tipus':"Tipus2", "subtipus":'Veri', "Moviment": 'Especial', 'categoria': 'Zafir'},
 6:{'tipus':"Tipus2","subtipus":'foc',"Moviment":"Normal",'categoria':'Categoria0'},
 7:{'tipus':"Tipus2","subtipus":'volador',"Moviment":"Normal",'categoria':'Categoria0'},
 8:{'tipus':"Tipus3","subtipus":'Aigua',"Moviment":"Normal",'categoria':'Categoria0'},
 9:{'tipus':"Tipus3","subtipus":'Bitxo',"Moviment":"Normal",'categoria':'Categoria0'}
}
participants={
 1:{'nom':'pc','punts':12,'numpartides':7,'pokemon':4,'energia':[145,25,36,256,968,9,546]},
 2:{'nom':'Ana123','punts':3,'numpartides':1, 'pokemon':1,'energia':[335,75,326]},
 3:{'nom':'Marta','punts':10,'numpartides':5,'pokemon':3,'energia':[119,358,471,88,44]},
 4:{'nom':'Marta','punts':23,'numpartides':1,'pokemon':3,'energia':[921]},
 5:{'nom':'Marta','punts':57,'numpartides':1,'pokemon':2,'energia':[43]},
 6:{'nom':'pc','punts':2,'numpartides':1,'pokemon':1,'energia':[26]},
 7:{'nom':'pc','punts':2,'numpartides':5,'pokemon':1, 'energia':[64,712,855,269,358]},
 8:{'nom':'Ana123','punts':33,'numpartides':1, 'pokemon':1, 'energia':[329]},
 9:{'nom':'Pokemito','punts':250,'numpartides':1, 'pokemon':3, 'energia':[651]},
 10:{'nom':'Juanito23','punts':14,'numpartides':1, 'pokemon':2, 'energia':[964]},
 11:{'nom':'pokemazo','punts':26,'numpartides':1, 'pokemon':1, 'energia':[836]}
}


while True:
  while True:
      print("1.- Escull pokemon\n2.- Generar pokemon pc\n3.- Començar la batalla\n4.- Puntuació total de cada participant\n"
            "5.- Mostrar els 3 primers guanyadors\n6.- Mostrar el pokemon que més partides ha guanyat\n7.- Sortir")
      opc = input("Opcion: ")
      if not opc.isdigit():
          print("Opcion Invalida")
      elif int(opc) < 1 or int(opc) > 7:
          print("Opcion Invalida")
      else:
          break
   if opc == "1":
       print(1)
   elif opc == "2":
    print(2)
   elif opc == "3":
    print(2)
   elif opc == "4":
    print(2)
   elif opc == "5":
    print(2)
   elif opc == "6":
    for i in participants:
     print(participants[i])
   elif opc == "7":
       print("Saliendo...")
       break
