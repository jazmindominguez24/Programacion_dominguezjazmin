import random

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 40

    def atacar(self, enemigo):
        daño = random.randint(5, 10)
        enemigo.vida -= daño
        print(self.nombre, "hace", daño, "de daño")

jugador = Personaje(input("Tu nombre: "))
enemigo = Personaje("Sistema")

turnos = 5

for i in range(turnos):
    if jugador.vida <= 0 or enemigo.vida <= 0:
        break

    print("Turno", i+1)
    print("Tu vida:", jugador.vida)
    print("Vida enemigo:", enemigo.vida)

    input("Presione el enter para atacar")
    jugador.atacar(enemigo)

    if enemigo.vida > 0:
        enemigo.atacar(jugador)


if jugador.vida > enemigo.vida:
    print("Ganaste")
else:
    print("Perdiste")

