def es_potencia(n:int,b:int)->int:
    exponente=0
    base=0
    while base < n:
        base=b**exponente
        print(base)
        if base == n:
            return True
        exponente+=1
    return False

n= int(input("ingrese n: "))
b=int(input("ingrese b: "))
print(es_potencia(n,b))