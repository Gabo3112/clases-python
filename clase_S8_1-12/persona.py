class persona:
    def __init__(self) -> None:
        self.nombre=input("ingrese nombre: ")
        self.sexo=input("ingrese sexo: ")
        self.edad=input("ingrese su edad: ")
        self.tipo="no identificado"

    def imprimir(self)->None:
        print("nombre: ",self.nombre)
        print("edad: ",self.edad)
        print("sexo: ",self.sexo)
        print("tipo: ",self.tipo)

    def funcion_principal(self)->None:
        pass
    