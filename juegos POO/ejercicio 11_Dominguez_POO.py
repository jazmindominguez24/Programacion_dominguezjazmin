import random

class Hechicero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.mana = 50

    def atacar(self, enemigo):
        if self.mana >= 10:
            daño = random.randint(10, 25)
            enemigo.vida -= daño
            self.mana -= 10
            print(f"{self.nombre} hace {daño}")
        else:
            print("Sin mana")

    def recargar(self):
        self.mana += 10
        print("Recarga mana")

jugador = Hechicero("Jugador")
cpu = Hechicero("CPU")

while jugador.vida > 0 and cpu.vida > 0:
    print("\n1.Atacar 2.Recargar")
    op = input("Elegí: ")

    if op == "1":
        jugador.atacar(cpu)
    elif op == "2":
        jugador.recargar()

    cpu.atacar(jugador)

    print(jugador.vida, jugador.mana)
    print(cpu.vida, cpu.mana)

print("GAME OVER")