class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.l1 = lado1
        self.l2 = lado2
        self.l3 = lado3

    def lado_mayor(self):
        print("Lado mayor:", max(self.l1, self.l2, self.l3))

    def tipo(self):
        if self.l1 == self.l2 == self.l3:
            print("Triangulo equilátero")
        elif self.l1 == self.l2 or self.l1 == self.l3 or self.l2 == self.l3:
            print("Triangulo isosceles")
        else:
            print("Triangulo escaleno")

t = Triangulo(3, 4, 4)
t.lado_mayor()
t.tipo()