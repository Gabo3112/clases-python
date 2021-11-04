from math import pow

def suma(a,b):
    return a+b
    
    
def resta(a,b):
    return a-b
    

def multiplicacion(a,b):
    return  a*b
    

def division(a,b):
    return a/b
     
def portencia(a,b):
    return pow(5,1)

def fib(n):
    a, b, c = 0, 1, 0
    while b < n:
        print(b, end=" ")
        #c = b
        #b= a + b
        #a = c
        a, b=b, a + b
    print()
#para formatear
#%s texto o cadena
#%d decimales o numeros
def imprimir(operacion, resultado ):
    print("la es %s: "% (operacion, resultado) )
