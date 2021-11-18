class sala:

    nroSala: int
    pelicula: str
    aforo: int 

def __init__(self)-> None:
    self.nroSala =int(input("ingrese numero de la sala: "))
    self.pelicula=input("nombre de la pelicula: ")
    self.aforo=int(input("ingrese el aforo de la sala: "))

def mostrar_datos(self)-> None:
    print("numero de la sala: ",self.nroSala)
    print("nombre de la pelicula: ",self.pelicula)
    print("numero de aforo: ",self.aforo)
