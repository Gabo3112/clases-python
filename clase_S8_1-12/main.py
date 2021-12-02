from persona import persona
from alumno import alumno
from docente import docente

print("**************registrar persona****************")
persona1= persona()
print()

print("*************registrar alumno*****************")
alumno1=alumno()
print()

print("*************registro docente***************")
docente1=docente()
print()

##OVERLOADING sobrecarga de metodos con herencia - REUTILIZACION
print("**************imprimiendo datos ingresados*************")
print("=============persona:============== ")
persona1.imprimir()
print("================alumno:================ ")
alumno1.imprimir()
print("==============docente:================ ")
docente1.imprimir()

#sobreescritura 
print("*******funciones principales**************")
persona1.funcion_principal()
alumno1.funcion_principal()
docente1.funcion_principal()