from figura import figura

class rombo(figura):

    def __init__(self) -> None:
        super().__init__()
        self.nombre_fig="rombo"
        self.nro_lados=4
        self.color="rojo"
        self.dg_mayor=int(input("ingrese diagonal mayor: "))
        self.dg_menor=int(input("ingrese diagonal menor: "))

    def calcular_area(self)->None:
        return (self.dg_mayor * self.dg_menor)/2