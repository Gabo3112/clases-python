from figura import figura

class triangulo(figura):

    def __init__(self) -> None:
        super().__init__()
        self.nombre_fig="triangulo"
        self.nro_lados=3
        self.color="amarillo"
        self.base=int(input("ingrese base: "))
        self.altura=int(input("ingrese altura: "))

    def calcular_area(self)->None:
        return (self.base * self.altura)/2
