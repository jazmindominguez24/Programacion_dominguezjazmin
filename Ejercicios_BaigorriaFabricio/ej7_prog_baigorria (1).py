class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")


class CajaAhorro(Cuenta):
    def mostrar(self):
        self.imprimir()


class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def calcular_interes(self):
        return self.cantidad*self.interes / 100

    def mostrar(self):
        self.imprimir()
        print(f"Plazo: {self.plazo}")
        print(f"Interés: {self.interes}")
        print(f"Interés ganado: {self.calcular_interes()}")

caja = CajaAhorro("Juani", 1000)
caja.mostrar()

plazo = PlazoFijo("Facu", 2000, 12, 5)
plazo.mostrar()