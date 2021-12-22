############## SIN USO DE LAMBDAS ####################
# def sumar(a,b):
#     return a+b
# print("5+3= ",sumar(5,3))

############### CON USO DE LAMBDAS ######################
# lambda: funcion que recibe uno o mas parametros pero siempre va a devolver un valor
sum=lambda a,b : a+b
resultado=lambda a,b: "{}+{}={}".format(a,b,sum(a,b))
print(resultado(int(input("primer valor: ")), int(input("segundo valor: "))))

# x= lambda x: "el valor es: "+ x
# print(x(input("ingrese un valor: ")))



mayor_edad= lambda edad : "es mayor de edad" if edad > 18 else "no es mayor de edad"
print(mayor_edad(int(input("ingrese su edad: "))))


# import datetime

# def mayor_edad():
#     #ingrese su fecha de nacimiento
#     fec_nac=input("ingrese fecha nacimiento: ")
    
#     #calcular su edad
#     print(datetime.datetime.today())
    
#     #devolver si es mayor de edad
    
# mayor_edad()
