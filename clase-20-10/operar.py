#uso de la calculadora
#primera operacion con 20 y 4

import calculadora
calculadora.imprimir("sumar", calculadora.suma(20,4))
calculadora.imprimir("restar", calculadora.resta(20,4))
calculadora.imprimir("multiplicar", calculadora.multiplicacion(20,4))
calculadora.imprimir("dividir", calculadora.division(20,4))

#resolver(3+5)*10
calculadora.imprimir("operacion", calculadora.multiplicacion(calculadora.suma(3,5),10))

#tarea: crear el archivo operacio_combinada.py que permita leer una cadena que representa los calculos que se deben
#debe realizar con el modulo de calculadora. Minimo debe permitir trabajar con 3 numero. debe imprimir el resultado de la operacion 
#ejemplo: 4+5*10=54
#en caso se ingrese una cadena que no se puede operar imprimir un mensaje de error