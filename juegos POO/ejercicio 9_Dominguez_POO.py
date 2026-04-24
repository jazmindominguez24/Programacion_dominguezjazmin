import random

class Cofre:
    def __init__(self):
        self.abierto = False
        self.monedas = random.randint(10, 50)

    def abrir(self):
        if not self.abierto:
            self.abierto = True
            print(f"Abriste el cofre. Tiene {self.monedas} monedas")
        else:
            print("El cofre ya estaba abierto")

class Explorador:
    def __init__(self):
        self.monedas = 0

    def recolectar(self, cofre):
        if cofre.abierto and cofre.monedas > 0:
            self.monedas += cofre.monedas
            print(f"Recolectaste {cofre.monedas} monedas")
            cofre.monedas = 0
        else:
            print("No hay monedas para recolectar")


jugador = Explorador()

for i in range(3):  
    print(f"\nEntraste a una sala {i+1}")
    cofre = Cofre()

    while True:
        print("\n1. Abrir cofre")
        print("2. Recolectar monedas")
        print("3. Continuar explorando")
        op = input("Elegí: ")

        if op == "1":
            cofre.abrir()
        elif op == "2":
            jugador.recolectar(cofre)
        elif op == "3":
            break
        else:
            print("Opción inválida")

        print("Monedas totales:", jugador.monedas)

print("Exploración terminada")
print("Monedas finales:", jugador.monedas)
print("GAME OVER")