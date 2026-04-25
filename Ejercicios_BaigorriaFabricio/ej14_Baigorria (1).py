import random

class Torre:
    def __init__(self):
        self.vida = 50

    def recibir_ataque(self):
        daño = random.randint(5, 15)
        self.vida -= daño
        print("La torre recibe", daño, "de daño")


torre = Torre()

while torre.vida > 0:
    print("Vida torre:", torre.vida)
    input("presione el enter para atacar")
    torre.recibir_ataque()

print("La torre se cayó")
