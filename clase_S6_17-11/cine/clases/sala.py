from clases.espectador import espectador
class sala:

    nroSala: int
    pelicula: str
    aforo: int 
    espectadores=[]

    def __init__(self)-> None:
        self.nroSala =int(input("ingrese numero de la sala: "))
        self.pelicula=input("nombre de la pelicula: ")
        self.aforo=int(input("ingrese el aforo de la sala: "))

    def mostrar_datos(self)-> None:
        print("numero de la sala: ",self.nroSala)
        print("nombre de la pelicula: ",self.pelicula)
        print("numero de aforo: ",self.aforo)

    def ingresarEspectadores(self, espectador: espectador)->None:
        if len(self.espectadores)< self.aforo:
            self.espectadores.append(espectador)
        else:
            print("la sala esta llena")

    def listarEspectador(self)->None:
        for esp in self.espectadores:
            print("la sala {} tiene {}: ".format(self.nroSala, len(self.espectadores)))
            esp.imprimirDatos()
            #(espectador)(esp).imprimirDatos()