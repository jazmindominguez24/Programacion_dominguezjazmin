class Cuenta:
    def cargar(self):
        self.titular = input("Titular: ")
        self.cantidad = float(input("Cantidad: "))

    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)

class CajaAhorro(Cuenta):
    def mostrar(self):
        print("Caja de Ahorro")
        super().mostrar()

class PlazoFijo(Cuenta):
    def cargar_datos(self):
        super().cargar()
        self.plazo = int(input("Plazo (días): "))
        self.interes = float(input("Interés (%): "))

    def calcular_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar(self):
        print("Plazo Fijo")
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)
        print("Plazo:", self.plazo)
        print("Interés:", self.interes)
        print("Ganancia:", self.calcular_interes())

caja = CajaAhorro()
caja.cargar()
caja.mostrar()
plazo = PlazoFijo()
plazo.cargar_datos()
plazo.mostrar()