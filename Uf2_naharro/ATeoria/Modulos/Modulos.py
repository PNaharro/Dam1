#Esto cuando estan en la misma carpeta
# import Definiciones, Definiciones2 as def2
# print(Definiciones.miSuma(5,6))
# print(def2.saludo())
# from Definiciones import miSuma
# print(miSuma(4,6))

# import Definiciones.Definiciones
# import Definiciones.Definiciones as Def1
# #Con as
# print(Def1.miSuma(5,4))
# #Sin as
# print(Definiciones.Definiciones.miSuma(5,4))


import Definiciones.Saludos.MisSaludos as S
S.saludosEsp()
S.saludosIng()
