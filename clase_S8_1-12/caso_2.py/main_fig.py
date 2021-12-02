from rombo import rombo
from triangulo import triangulo
from cuadrado import cuadrado
from circulo import circulo

print("********datos del cuadrado********")
cuad=cuadrado()
print("********datos del triangulo********")
trian=triangulo()
print("********datos del rombo********")
rom=rombo()
print("********datos del circulo********")
cir=circulo()

print("***********datos de las figuras************")

print("**datos del cuadrado")
cuad.mostrar_datos()
print("su area es",cuad.calcular_area())
print("el perimetro es",cuad.calcular_perimetro())
print()


print("**datos del triangulo**")
trian.mostrar_datos()
print("su area es",trian.calcular_area())
print()

print("**datos del circulo**")
cir.mostrar_datos()
print("el area es",cir.calcular_area())
print()


print("**datos del rombo**")
rom.mostrar_datos()
print("el area es",rom.calcular_area())
print()


