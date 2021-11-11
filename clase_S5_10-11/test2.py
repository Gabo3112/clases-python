# ejemplo de la clase animal
class animal:

    def __init__(self) -> None:
        self.nombre=input("ingrese nombre: ")
        self.grupos=input("grupo: ")

    def desplazamiento(self):
        if (self.grupos=='ave'):
            "se desplaza volando"
        elif self.grupos=='serpiente':
            return"se despaza arrastrando"
        else:
            return"se desplaza caminando"

# perro = animal()
# gato= animal()
# boa=animal()
# aguila=animal()

# print("el {} {}".format(perro.nombre,perro.desplazamiento()))
# print("el {} {}".format(gato.nombre,gato.desplazamiento()))
# print("el {} {}".format(boa.nombre,boa.desplazamiento()))
# print("el {} {}".format(aguila.nombre,aguila.desplazamiento()))

#crear una lista con 5 animales y de los animales ingresados hagan andar al primero y al ultimo de la lista

animales=[]
for i in range(5):
    animales.append(animal())

print("el primer animal: ",animales[0].desplazamiento())
print("el ultimo animal: ",animales[len(animales)-1].desplazamiento())