from banca.banco import banco
class cliente:
    def __init__(self) -> None:
        self.nombre=input("nimbre del cliente: ")
        self.saldo=0.0

    def depositar(self,monto)-> None:
        #self.saldo = self.saldo + monto
        monto=float(input("monto a depositar: "))
        self.saldo+=monto

    def retirar(self,monto)->None:
        monto=float(input("monto a retirar: "))
        
        if self.consultar_saldo()>=monto:
            self.saldo-=monto
        else:
            print("saldo insuficiente")  

    def transferir(self)->None:
        monto=float(input("monto a transferir: "))
        nombre_receptor=input("cliente a transferir: ")
        cliente_receptor=bco.buscar_cliente(nombre_receptor)
        if bco.buscar_cliente(nombre_receptor)!=None:
            self.saldo-=monto
            cliente_receptor.saldo+=monto


    def consultar_saldo(self)->float:
        return self.saldo
