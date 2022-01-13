number=int(input("numero a calcular factorial: "))

#algoritmo sin recursividad para calcular factorial
# fact=1
# for i in range(1,number + 1 ,1):
#     fact*=i
# print("el factorial de {}=  {}".format(number,fact))


#algoritmo usando recursividad para calcular factorial
#1. debe de invocar al mismo metodo
#2. siempre retorna un valor
#3. para evitar el bucle infinito, debe tener un punto de corte
def factorial(n: int) -> int:
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
fact=factorial(number)    
print("el factorial de {}=  {}".format(number,fact))

