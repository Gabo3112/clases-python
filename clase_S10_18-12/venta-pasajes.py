
# Ingresar los pasajeros
from pasajero import pasajero

def main_menu():
    print("******Menu principal*******")
    print("[1]agregar pasajero")
    print("[2] mostrar pasajeros")
    print("[3] vender pasajeros")
    print("[x] salir")

def listar_pasajeros():
    f_pasajeros=open("pasajeros.text", "r")
    line=f_pasajeros.readlines()
    for line in lines:
        print(line)

while True:
    main_menu()
    opc=input("ingrese opcion: ")
    if opc=="1":
        pasajeros = pasajero()
        pasajeros.grabar()
    elif opc =="2":
        print("lista de pasajeros")
        pasajeros.listar()
    else:
        break



# Crear el archivo pasajeros
file = open("pasajeros.txt", "w")
file.close

for i in range(5):
    pasajero = pasajero()
    pasajero.grabar()