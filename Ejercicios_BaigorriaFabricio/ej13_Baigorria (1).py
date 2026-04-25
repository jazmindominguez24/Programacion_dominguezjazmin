import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def tirar_dado(self):
        dado = random.randint(1, 6)
        self.puntos += dado
        print(self.nombre, "sacó", dado)


jugador = Jugador("Vos")
cpu = Jugador("CPU")

for i in range(5):
    input("presione el enter para tirar el dado")
    jugador.tirar_dado()
    cpu.tirar_dado()

print("Puntaje final:", jugador.puntos, "-", cpu.puntos)

if jugador.puntos > cpu.puntos:
    print("Ganaste")
else:
    print("Perdiste")

