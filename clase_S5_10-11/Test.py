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
    nro_ruedas=4
    def __init__(self,marca,anio_fabricacion):
        self.marca=marca
        self.anio_fabricacion=anio_fabricacion
    def mostrasDtos(self):
        print("es un vehiculo de la marca {}, con año de fabricacion {}, el numero de ruedas es {}".format(self.marca,
        self.anio_fabricacion,self.nro_ruedas))


#CREAR UN OBJETO DE LA CLASE PERSONA-INSTACIAR
pedro="es una persona"
juan=Personas()

print(pedro)
print("nombre: {}, edad: {}, sexo: {}".format(juan.nombre,juan.edad,juan.sexo))

#creacion de 2 objetos de la clase vehiculo
veh1= Vehiculo("toyota",2010)
veh2= Vehiculo("kia",2019)
veh3= Vehiculo("Honda",2020)
marca=input("ingrese marca del vehiculo: ")
anio_fabricacion=input("ingrese año de fabricacion del vehiculo: ")
veh4=Vehiculo(marca,anio_fabricacion)
veh4.nro_ruedas=2
#se esta invocando el metodo mostrarDtos() de los vehiculos creados
veh1.mostrasDtos()
veh2.mostrasDtos()
veh3.mostrasDtos()
veh4.mostrasDtos()


