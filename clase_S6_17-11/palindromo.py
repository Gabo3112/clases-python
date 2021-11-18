from estructura import clase

palabra=input("ingrese palabra: ")
pila1=clase.pila()
pila2=clase.pila()

# for i in range(len(palabra)):
#     pila1.push(i)

for letra in palabra:
    pila1.push(letra)

cont=0
for letra in palabra:
    letraAux=pila1.pop()
    if letra== letraAux:
        cont+=1

if cont == len(palabra):
    print("si es palindromo ")
else:
    print("no es palindromo")

#print(pila1)