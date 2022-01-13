from types import DynamicClassAttribute


class persona:

    def __init__(self, id , nombre, DNI, nacionalidad) -> None:
        self.id= id 
        self.nombre= nombre
        self.dni= DNI
        self.nacionalidad = nacionalidad