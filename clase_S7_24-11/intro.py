##  REPADO DE METODOS PROPIOS DE PYTHON
# cadena="1,2,3,4,5"
# list=cadena.split(",")
# print(cadena)
# print(list)

#################################################################
# # USO DEL METODO __init__ DE UNA CLASE
# from persona import persona

# print("******* persona uno ********")
# persona1=persona()
# persona1.imprimir_datos()
# persona1.imprimir_mayor_edad()
# persona1.mayor_edad()
# persona1.tramitir_licencia()


# print("******* persona dos ********")
# persona2=persona()
# persona2.imprimir_datos()
# persona2.imprimir_mayor_edad()
# persona2.mayor_edad()
# persona2.tramitir_licencia()

#################################################################
from banca import cliente
from banca import banco

bco=banco()
#cliente1=cliente()
cliente1=bco.cliente1
cliente1.depositar()
cliente1.retirar()
cliente1.depositar()
print("el saldo del cliente {} es {}".format(cliente1.nombre, cliente1.consultar_saldo()))


#cliente1=cliente()
cliente2=bco.cliente1
cliente2.depositar()
cliente2.retirar()
cliente2.depositar()
print("el saldo del cliente {} es {}".format(cliente2.nombre, cliente2.consultar_saldo()))


#cliente3=cliente()
cliente3=bco.cliente1
cliente3.depositar()
cliente3.retirar()
cliente3.depositar()
print("el saldo del cliente {} es {}".format(cliente3.nombre, cliente3.consultar_saldo()))

print("")

