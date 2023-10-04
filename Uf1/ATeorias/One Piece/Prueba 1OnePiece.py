dicc_players = {1:{"nombre":"Luffy","categoria":1,"armas":[1,1],"fuerza":6,"velocidad":7,"experiencia":0},
                2:{"nombre":"Zoro","categoria":1,"armas":[4],"fuerza":5,"velocidad":6,"experiencia":0},
                3:{"nombre":"Sanji","categoria":1,"armas":[1,3],"fuerza":4,"velocidad":6,"experiencia":0},
                4: {"nombre": "Buggy", "categoria": 2, "armas": [3], "fuerza": 2, "velocidad": 4, "experiencia": 0},
                5: {"nombre": "Mr3", "categoria": 2, "armas": [5], "fuerza": 3, "velocidad": 2, "experiencia": 0},
                6: {"nombre": "Xebec", "categoria": 3, "armas": [1, 3], "fuerza": 6, "velocidad": 5, "experiencia": 0},
                7: {"nombre": "Kaido", "categoria": 3, "armas": [4], "fuerza": 8, "velocidad": 3, "experiencia": 0},
                8: {"nombre": "Mama grande", "categoria": 3, "armas": [5], "fuerza": 7, "velocidad": 1, "experiencia": 0},
                9: {"nombre": "Akainu", "categoria": 4, "armas": [2], "fuerza": 6, "velocidad": 4, "experiencia": 0},
                10: {"nombre": "Kizaru", "categoria": 4, "armas": [1, 3], "fuerza": 5, "velocidad": 8, "experiencia": 0},
                11: {"nombre": "Fujitora", "categoria": 4, "armas": [5], "fuerza": 5, "velocidad": 4, "experiencia": 0},
                12: {"nombre": "Garp", "categoria": 5, "armas": [2], "fuerza": 6, "velocidad": 3, "experiencia": 0},
                13: {"nombre": "Smoker", "categoria": 5, "armas": [5], "fuerza": 5, "velocidad": 5, "experiencia": 0},
                14: {"nombre": "Koby", "categoria": 6, "armas": [4], "fuerza": 3, "velocidad": 4, "experiencia": 0},
                15: {"nombre": "Tashigi", "categoria": 6, "armas": [3], "fuerza": 4, "velocidad": 4, "experiencia": 0},
                }
dicc_weapons = {1:{"nombre":"Espada","fuerza":3,"velocidad":5,"dos_manos":False},
                2:{"nombre":"Gran Espada","fuerza":5,"velocidad":3,"dos_manos":True},
                3: {"nombre": "Pistola", "fuerza": 2, "velocidad": 6, "dos_manos": False},
                4: {"nombre": "Rifle", "fuerza": 3, "velocidad": 4, "dos_manos": True},
                5: {"nombre": "Chuchi", "fuerza": 4, "velocidad": 4, "dos_manos": True}
                }
dicc_crews = {1:{"nombre":"Straw Hat","miembros" : [8,6]},
              2: {"nombre": "Pirates Buggy", "miembros": [1,3,5]},
              3: {"nombre": "Pirates Ricks", "miembros": [2,4,7]}
              }
dicc_ranks = {1:{"nombre":"Admiral","miembros":[9,10,11]},
              2:{"nombre":"ViceAdmiral","miembros":[12,13]},
              3:{"nombre":"lieutenant","miembros":[14,15]}
              }
dicc_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}

# Listar por Velocidad
menu0414 = "=" * 14 + "Personajes ordenados por Velocidad" + "=" * 13 + "\n" + "ID".ljust(
    10) + "Nombre".ljust(15) \
           + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
print(menu0414)
listaVlz = []
listaKys = []
for i in dicc_players:
    for j in dicc_players[i]["armas"]:
        dicc_players[i]["fuerza"] += dicc_weapons[j]["fuerza"]
        dicc_players[i]["velocidad"] += dicc_weapons[j]["velocidad"]
    listaVlz.append(dicc_players[i]["velocidad"])
    listaKys.append(i)

for i in range(len(listaVlz) - 1):
    for j in range(len(listaVlz) - i - 1):
        if listaVlz[j] < listaVlz[j + 1]:
            numero = listaVlz[j]
            listaVlz[j] = listaVlz[j + 1]
            listaVlz[j + 1] = numero

            numero = listaKys[j]
            listaKys[j] = listaKys[j + 1]
            listaKys[j + 1] = numero
for n in listaKys:
    string_velocidad = str("{}".format(n)).ljust(10) + str(dicc_players[n]["nombre"]).ljust(
        20) + str(dicc_players[n]["fuerza"]).ljust(13) \
                    + str(dicc_players[n]["velocidad"]).ljust(17) + str(
        dicc_players[n]["experiencia"])
    print(string_velocidad)
input()
