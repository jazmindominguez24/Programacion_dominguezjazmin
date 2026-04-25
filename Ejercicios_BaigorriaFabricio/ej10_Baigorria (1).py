import random

class Auto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 0

    def avanzar(self):
        pasos = random.randint(1, 6)
        self.posicion += pasos

jugador = Auto("Tu auto")
rival = Auto("Rival")

meta = 30

while jugador.posicion < meta and rival.posicion < meta:
    print("\nTu posicion:", jugador.posicion)
    print("Rival:", rival.posicion)

    input("Presione el enter para avanzar")

    jugador.avanzar()
    rival.avanzar()

if jugador.posicion >= meta:
    print("Ganaste")
else:
    print("Perdiste")

