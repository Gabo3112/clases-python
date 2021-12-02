class figura:

    def __init__(self) -> None:
        self.nombre_fig=""
        self.nro_lados=0
        self.color="sin color"

    def mostrar_datos(self)->None:
        print("figura: ",self.nombre_fig)
        print("lados: ",self.nro_lados)
        print("color: ",self.color)

    def calcular_perimetro(self)-> float:
        pass

    def calcular_area(self)-> float:
        pass    

    