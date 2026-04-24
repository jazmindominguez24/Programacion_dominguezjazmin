import random

class Aventurero:
    def __init__(self):
        self.inventario = []

    def guardar(self, obj):
        self.inventario.append(obj)
        print(f"Guardaste {obj}")

    def usar(self):
        if self.inventario:
            obj = self.inventario.pop(0)
            print(f"Usaste {obj}")
        else:
            print("No hay objetos")

    def ver(self):
        print("Inventario:", self.inventario)

objetos = ["espada", "poción", "oro", "escudo"]

jugador = Aventurero()

for i in range(5):
    print("\nExplorando...")
    encontrado = random.choice(objetos)
    print("Encontraste:", encontrado)

    print("1. Guardar")
    print("2. Usar algo")
    print("3. Ignorar")
    print("4. Ver inventario")

    op = input("Elegí: ")

    if op == "1":
        jugador.guardar(encontrado)
    elif op == "2":
        jugador.usar()
    elif op == "4":
        jugador.ver()

print("Fin de la aventura")
jugador.ver()
print("GAME OVER")