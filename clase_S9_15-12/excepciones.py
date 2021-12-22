# try: 
#     a=int(input("ingrese numero: "))
#     div=a/5

# except KeyboardInterrupt:
#     print("esta intentando finalizar el programa")
# except :
#     print("estimado usuario, ocurrio un error")
# else:
#     print("el programa se realizo con exito")
# finally:
#     print("finalizo el programa")


# class TamanioDNI(Exception):

#     def __init__(self, dni) -> None:
#         super().__init__(self)
#         self.dni=dni
#         self.tamanio=len(dni)

#     def get_message(self)-> str:
#         # return "DNI incorrecto. DNI actual tiene {} caracteres".format(td.tamanio)
#         return "DNI incorrecto. DNI actual tiene " +format(td.tamanio)+ "caracteres"


# try:
#     dni=input("ingrese DNI: ")
#     if(len(dni) != 8 ):
#         raise TamanioDNI(dni)

# except TamanioDNI as td:
#     print(td.get_message())


################ ASSERT #####################

# try:
#     print("ejemplo de assert")
#     assert 1==1
#     print("fin del ejemplo")

# except AssertionError:
#     print("se interrumpio el programa")




# try:
#     list=[0,1,2,3,4,5,6]
#     print(list)
#     while True:
#         list.pop()
#         assert len(list) > 1
#         print(list)
# except AssertionError:
#     print("error")


