import random

class Auto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.distancia = 0

    def avanzar(self, min, max):
        paso = random.randint(min, max)
        self.distancia += paso
        print(f"{self.nombre} avanza {paso}")

meta = 50

jugador = Auto("Jugador")
cpu = Auto("CPU")

while jugador.distancia < meta and cpu.distancia < meta:
    print("\n1. Lento (seguro)")
    print("2. Normal")
    print("3. Rápido (riesgoso)")
    op = input("Elegí: ")

    if op == "1":
        jugador.avanzar(1, 3)
    elif op == "2":
        jugador.avanzar(2, 5)
    elif op == "3":
        if random.random() < 0.3:
            print("Te accidentaste! No avanzas")
        else:
            jugador.avanzar(4, 8)
    else:
        print("Opción inválida")
        continue

    cpu.avanzar(2, 6)

    print(f"Posiciones -> Jugador: {jugador.distancia} | CPU: {cpu.distancia}")
if jugador.distancia >= meta:
    print("GANASTE LA CARRERA")
else:
    print("PERDISTE LA CARRERA")

print("GAME OVER")