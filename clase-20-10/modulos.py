#import calculadora
#calculadora.imprimir("suma",50)
from calculadora import resta, imprimir, suma

imprimir("Suma",suma(100, 20))
imprimir("Resta", resta(300, 100))

import random
imprimir("Random", random.randint(1,100))