#pilas de una lista
#lista es un arreglo
#metodo
# lista=[]
# lista.append("Piura") #append: agregar un elemento
# lista.append("Sullana")
# lista.append("Talara")
# lista.append("Ayabaca") 
# lista.append("paita")
# print(lista)
# print("la lista tiene {} elementis".format(len(lista))) #len: tamaño de la lista

# lista.pop()        #pop: remueve el ultimo elemento
# print("se elimino el ultimo elemento de la lista. lista actual: ",lista)

# ciudad=input("ingrese ciudada a buscar: ")
# print("la ciudad {} se encuentra en la posicion {} ".format(ciudad, lista.index(ciudad)))

# lista.remove(ciudad)
# print("se procede a eliminar {} de la lista. la lista actualizada es: {} ".format(ciudad, lista))


# PILAS
# LIFO: Last-In, First-out

# #pila de monedas
# import pila
# #apilamiento de monedas
# pila.push("S/5")
# pila.push("S/2")
# pila.push("S/1")
# print(pila.lista)
# print(pila.pop())

from estructura import clase

monedas = clase.pila()
monedas.push("5")
monedas.push("2")
monedas.push("1")

print(monedas.items)

'''un almacen tiene capacidad para apilar n contenedores. cada contenedor
tiene un numero de identificacion. cuando se desea retirar un contenedor 
especificso, deben retirarse primero los contenedores que estan encima de el
y colocarlos en otra pila, efectuar el retiro y regresarlos'''


