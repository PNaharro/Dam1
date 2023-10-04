# variable1 = 10
# def funcion1():
#     global variable1
#     variable1 = 100
#     def sub_funcion1():
#         global variable1
#         variable1 = 1000
#     sub_funcion1()
#     print(variable1)
# # funcion1()
# # print(variable1)
#
# a=100
# def funcionA():
#     b=0
#     a = 1
#     print(a)
# funcionA()


a = 10
def prueba1():
    a = 100
    print(a)
    def prueba2():
        global a
        a = 1000
        print(a)
    prueba2()
prueba1()
print(a)