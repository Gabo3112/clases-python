from clases import sala

cantSala=int(input("ingrese cantidad de salas a programadas: "))
salas=[]

for i in range(cantSala):
    print("ingrese datos de la sala: ",(i+1))
    salas.append(sala.sala())

for Sala in salas:
    print("*****datos de la sala*******")
    Sala.mostrar_datos()

