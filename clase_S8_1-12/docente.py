from persona import persona

class docente(persona):

    def __init__(self) -> None:
        super().__init__()
        self.tipo="docente"
        self.uni_egreso=input("ingrese unividad donde egreso: ")

    def imprimir(self)->None:
        super().imprimir()
        print("universidad: ",self.uni_egreso)

    def funcion_principal(self)->None:
        print("su funcion principal es de enseñar")
