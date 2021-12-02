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

    # def transferir(self)->None:
    #     monto=float(input("monto a transferir: "))
    #     nombre_receptor=input("cliente a transferir: ")
    #     if nombre_receptor

    def consultar_saldo(self)->float:
        return self.saldo

class banco:
    def __init__(self) -> None:
        self.cliente1=cliente()
        self.cliente2=cliente()
        self.cliente3=cliente()
    def operaciones(self)->None:
        
        pass
        
    def deposito_total(self)->float:
        return self.cliente1.consultar_saldo()+self.cliente2.consultar_saldo()+self.cliente3.consultar_saldo()


