def ingreso():
    nombre=input("ingrese nombre: ")
    dni=input("ingrese dni: ")
    celular=input("ingre celular: ")
    return {"nombre":nombre,"dni": dni,"celular": celular }

def ver_datos(nombre,dni):
    print("la persona %s con dni %s"%(nombre,dni))