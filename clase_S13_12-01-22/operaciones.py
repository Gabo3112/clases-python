# pruebas unitarias (unit test)- converage (nivel de cobertura)
# pruebas unitarias son realizadas por el desarrollador 
#los analistas de calidad(QA) realizan pruebas manuales o pruebas autorizadas

def operar(operacion,a,b):
    if operacion=="+":
        return sumar(a,b)
    if operacion=="-":
        return restar(a,b)
    if operacion =="/":
        return dividir(a,b)
    print("operacion desconocida")
    return -1

def sumar(a,b):
    return a+b 

def dividir(a,b):
    return a/b

def restar(a,b):
    return a-b