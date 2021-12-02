from figura import figura

class circulo(figura):
    
    def __init__(self) -> None:
        super().__init__()
        self.nombre_fig="circulo"
        self.color="verde"
        self.radio= int(input("radio: "))

    def calcular_area(self) -> float:
        return 3.14 * self.radio

