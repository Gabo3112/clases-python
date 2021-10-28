from matematica import geometria  #segunda forma de importar
from matematica import calculadora

try:
    lado=int(input("ingresar el lado del cuadrado: "))
    print("el perimetro del cuadro de lado {} es {}".format(lado,geometria.perimetro_cuadrado(lado)))

    num1=int(input("ingrese un valor: "))
    num2=int(input("ingrese otro valor: "))
    print("la division de los numeros ingresados es: ", calculadora.division(num1,num2))

except TypeError:
    print("se ingreso un valor incorrecto")


except ZeroDivisionError:
    print("no es posible realizar una division por cero")
    #num2=1  
    #print("la division de los numeros ingresados es",calculadora,division(num1,num2))
    
except:
    print("se ingreso un valor incorrecto")