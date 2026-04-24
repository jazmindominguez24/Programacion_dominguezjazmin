import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, enemigo):
        daño = random.randint(5, self.ataque)
        daño_real = max(0, daño - enemigo.defensa)
        enemigo.vida -= daño_real
        print(f"{self.nombre} hace {daño_real} de daño")

    def defender(self):
        self.defensa += 2
        print(f"{self.nombre} aumenta defensa")

    def mostrar(self):
        print(f"{self.nombre}: Vida={self.vida}, Defensa={self.defensa}")


jugador = Personaje("Jugador", 100, 20, 5)
enemigo = Personaje("Enemigo", 100, 18, 4)

while jugador.vida > 0 and enemigo.vida > 0:
    print("\n1.Atacar  2.Defender  3.Ver estado")
    op = input("Elegí: ")

    if op == "1":
        jugador.atacar(enemigo)
    elif op == "2":
        jugador.defender()
    elif op == "3":
        jugador.mostrar()
        enemigo.mostrar()
        continue

    if enemigo.vida > 0:
        random.choice([enemigo.atacar, enemigo.defender])(jugador)

    jugador.mostrar()
    enemigo.mostrar()

print("GAME OVER")