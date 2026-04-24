class Triangulo:
    def cargar(self):
        self.lado1 = float(input("Lado 1: "))
        self.lado2 = float(input("Lado 2: "))
        self.lado3 = float(input("Lado 3: "))

    def mayor_lado(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print("Lado mayor:", mayor)

    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Isósceles")
        else:
            print("Escaleno")
t = Triangulo()
t.cargar()
t.mayor_lado()
t.tipo()