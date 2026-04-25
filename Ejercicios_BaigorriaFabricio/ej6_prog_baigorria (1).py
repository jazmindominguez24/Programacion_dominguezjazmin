class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        self.cantidad -= monto

    def mostrar_total(self):
        print(f"{self.nombre} tiene {self.cantidad}")


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Facu")
        self.cliente3 = Cliente("Fabri")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(200)
        self.cliente3.depositar(300)

        self.cliente1.extraer(50)

    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print("Total en el banco:", total)
        
banco = Banco()
banco.operar()
banco.deposito_total()

