from figura import figura

class cuadrado(figura):

    def __init__(self) -> None:
        super().__init__()
        self.nombre_fig="cuadrado"
        self.nro_lados=4
        self.color="azul"
        self.lado=int(input("ingrese lado: "))

    def calcular_perimetro(self)->None:
        return self.lado * self.lado

    def calcular_area(self)->None:
        return self.lado ** 2
