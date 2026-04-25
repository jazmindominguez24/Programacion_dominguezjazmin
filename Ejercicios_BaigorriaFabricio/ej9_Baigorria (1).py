class Cofre:
    def __init__(self, monedas):
        self.monedas = monedas
        self.abierto = False

    def abrir(self):
        if self.abierto == False:
            self.abierto = True
            return self.monedas
        else:
            return 0

cofre1 = Cofre(20)
cofre2 = Cofre(50)

total = 0

print("Hay 2 cofres")

op = input("Abrir cofre 1 o 2: ")

if op == "1":
    total += cofre1.abrir()
elif op == "2":
    total += cofre2.abrir()

print("Monedas obtenidas:", total)
