import matematica.calculadora #una forma de importar

a=5
b=3

print("{}+{}={}".format(a,b, matematica.calculadora.suma(a,b)))
print("{}-{}={}".format(a,b, matematica.calculadora.resta(a,b)))
print("{}*{}={}".format(a,b, matematica.calculadora.multiplicacion(a,b)))
print("{}/{}={}".format(a,b, matematica.calculadora.division(a,b)))
print("{}**{}={}".format(a,b, matematica.calculadora.potencia(a,b)))