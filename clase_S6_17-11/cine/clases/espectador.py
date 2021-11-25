class espectador:
    nombre: str
    tipo: str

    def __init__(self) -> None:
        self.nombre=input("ingrese su nombre: ")
        self.tipo=input("ingrese tipo de espectador: ")

    def imprimirDatos(self)-> None:
        print("nombre: ",self.nombre)
        print("tipo: ",self.tipo)