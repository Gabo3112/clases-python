############# CONCATENAR CADENAS ###################
"""cad1="bienvenido"
cad2="a Piura"
cal = "10"
print(cad1+cad2)
print(cad1+cad2+ cal)
print("{} {} {}".format(cad1,cad2, cal))"""

################ REPLICADO ####################
"""cad="hola"
cad2= 10
print(cad2*cad)
print(cad*9)"""

#################  chr() and ord()    ##################
"""print(ord("a"))
print(ord("A"))
print(chr(99))"""

############## CADENAS COMO LISTAS ######################
"""cadeba="estructura de datos"
for i in range(len(cadeba)):
    print(cadeba[i], end=" ")"""

#### REBANADAS #####
"""cadena="computadora"
#o: c 1:o
#parametros por defecto son [:::]
#start(inclusivo, defecto en 0),end(exclusivo, defecto en tamaño -1 ), step(por defecto 1)
print(cadena[2:5])#ut
print(cadena [5:])#tadora
print(cadena [:5])#compu
print(cadena [4:-2])#utado
#print(cadena[-10:7])#omputa
print(cadena[1:7:2])#opt
print(cadena[::2])#cmuaoa"""

### in #########
"""cad = "hola mundo "
find="ola"
print(cad not in find)"""

###### min() and max() ###########
"""num=[6,3,5]
cadena= "holamundo"
print(min(num))
print(min(cadena))
print(max(num))
print(max(cadena))"""

## find()   ##################
"""cadena= "bienvenidos a Piura"
find="piura"
print(cadena.find(find))"""

############# upper() lower() ##################################
"""cadena="hola mundo"
print(cadena.upper())
print(cadena.lower())"""

############## comparacion de cadenas  ####################
cad1="hola"
cad2="Hola"
print(cad1==cad2)
print(cad1 != cad2 ) 
print("10 " > "@10")