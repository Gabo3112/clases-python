"""def encriptar(val):
    num=["1","2","3","4","5","6"]
    if val in num:
        return val
    return None


val = input("ingrese un valor: ")
print("el valor ingresado es: ",val)"""
##############################################################
"""if encriptar(val) !=None:
    print("el valor encriptado es: ", len(encriptar(val)))
else: 
    print("no se logro encriptar ")"""
##############################################################

"""lista=[1,2,3]
if len(lista) > 0:
    print("Funcion pop de lista ", lista.pop())"""

#############EXCEPCION 1###################
"""try:
    num = int(input("ingrese un numero: "))
    print("{}/{}={}".format(num,10,num/10))
    lista=[1,2,3,4]
    print("elemento: ",lista[5])
    #print(str(num)+ "/10" + "=" +str(num/10))
except IndexError:
    print("indicde no encontrado")
except ValueError:
    print("error al ingresar el numero")
except:
    print("ocurrio un error inesperado")
else:
    print("se finalizo con exito")"""

################EXEPCION 2########################



while True:
    try:
        num=float(input("ingrese numero: "))
    except:
        print("valor ingresado es incorrecto")
    else:
        print("no se presento la excepcion ")
        break #se utiliza en secuencia repetitiva = while
    finally:
        print("fin del programa")



