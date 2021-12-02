from persona import persona

class alumno(persona):

    def __init__(self) -> None:
        super().__init__()
        self.tipo="alumno"
        self.grado=input("ingrese grado: ")

    def imprimir(self)->None:
        super().imprimir()
        print("grado: ",self.grado)

    def funcion_principal(self)->None:
        print("su funcion principal es estudiar")
    
