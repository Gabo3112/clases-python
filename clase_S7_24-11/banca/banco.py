from banca.cliente import cliente
class banco:
    def __init__(self) -> None:
        print("creando banco")
        self.cliente1=cliente()
        self.cliente2=cliente()
        self.cliente3=cliente()
        self.clientes=[]
        self.clientes.append(self.cliente1)
        self.clientes.append(self.cliente2)
        self.clientes.append(self.cliente3)

    def operaciones(self)->None:
        
        pass 

    def buscar_cliente(self)->None:
        

        
    def deposito_total(self)->float:
        return self.cliente1.consultar_saldo()+self.cliente2.consultar_saldo()+self.cliente3.consultar_saldo()
