#EL IDENTIFICADOR DE CLASE ES LA PALABRA class---------
#es una clase vacia
class Alumno:
    pass    #SE USA PARA DEFINIR UNA CLASE VACIA

#clase con atributos por defecto
class Personas:
    
    nombre="Pedro"
    edad=20
    sexo="masculino"

#es una clase con metodo de inicializacion que permite iniciar atributs con valores
#diferentes
class Vehiculo:
    def __init__(self,marca,anio_fabricacion):
        self.marca=marca
        self.anio_fabricacion=anio_fabricacion
    def mostrasDtos(self):
        print("es un vehiculo de la marca {}, con año de fabricacion {}".format(self.marca,self.anio_fabricacion))


#CREAR UN OBJETO DE LA CLASE PERSONA-INSTACIAR
pedro="es una persona"
juan=Personas()

print(pedro)
print("nombre: {}, edad: {}, sexo: {}".format(juan.nombre,juan.edad,juan.sexo))

veh1= Vehiculo("toyota",2010)
veh2= Vehiculo("kia",2019)
veh1.mostrasDtos()
veh2.mostrasDtos()



