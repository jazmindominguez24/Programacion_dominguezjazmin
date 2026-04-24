class Cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        self.cantidad=0
    def depositar(self,monto):
        self.cantidad+=monto
        
    def extraer(self,monto):
        self.cantidad-=monto
    def mostrar_total(self):
        print(self.nombre,"tiene",self.cantidad)
class Banco:
    def __init__(self):
        self.cliente1=Cliente("Isabella")
        self.cliente2=Cliente("Matias")
        self.cliente3=Cliente("Juan")
    def operar(self):
        self.cliente1.depositar(650000)
        self.cliente2.depositar(45000)
        self.cliente3.depositar(750000)
        self.cliente3.extraer(2450)
    def deposito_total(self):
        total=(self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad)
        print("total en el banco:",total)
banco=Banco()
banco.operar()
banco.deposito_total()