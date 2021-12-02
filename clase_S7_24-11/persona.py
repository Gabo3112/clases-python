class persona:
    def __init__(self) -> None:
        self.nombre= input("ingrese nombre: ")
        self.edad=int(input("ingrese su edad: "))
        self.estado_civil=input("ingrese estado civil (S|C|V|D): ")
    
    def mayor_edad(self)-> bool:
        # if (self.edad >=18):
        #     return True
        # else:
        #     return False
        # #un return corta el programa para devolver
        # if (self.edad >=18):
        #     return True
        # return False
        return self.edad>=18


    def imprimir_datos(self)-> None:
        print("nombre: ",self.nombre)
        print("edad: ",self.edad)
        print("estado civil: ",self.estado_civil)

    def imprimir_mayor_edad(self)-> None:
        if self.mayor_edad():
            print("es mayor de edad")
        else:
            print("no es mayor de edad")

    def tramitir_licencia(self)-> None:
        if self.mayor_edad() or(self.edad==16 and (self.estado_civil=="casado")):
            print("si puede tramitir licencia")
        else:
            print("no puede tramitir liecencia")

    #definir un metodo que indique si puede tramitar licencia de conducir
    #una persona puede tramitar una licencia si es mayor de edad o es casado
    #y tiene 16 años
