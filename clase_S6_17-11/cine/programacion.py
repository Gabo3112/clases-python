from clases.sala import sala
from clases.espectador import espectador

cantSala=int(input("ingrese cantidad de salas a programadas: "))
salas=[]

for i in range(cantSala):
    print("ingrese datos de la sala: ",(i+1))
    salas.append(sala())

for Sala in salas:
    print("*****datos de la sala*******")
    Sala.mostrar_datos()

#numero de espectador
print("primer espetacor") 
esp1=espectador()
#(sala)(salas[0]).ingresarEspectadores(esp1)
salas[0].ingresarEspectadores(esp1)

print("segundo espectador")
esp2=espectador()
#(sala)(salas[0]).ingresarEspectadores(esp2)
salas[0].ingresarEspectadores(esp2)

#(sala)(salas[0]).ingresarEspectadores()
salas[0].listarEspectador()