import random
class Torre:
    def __init__(self):
        self.vida = 100
        self.defensa = 0

    def defender(self):
        self.defensa = 5
        print("La torre se prepara para defender (reduce daño)")

    def reparar(self):
        self.vida += 10
        print("Reparaste la torre (+10 vida)")

    def recibir_ataque(self):
        daño = random.randint(10, 25)
        daño_real = max(0, daño - self.defensa)
        self.vida -= daño_real
        print(f"Recibís {daño_real} de daño")
        self.defensa = 0  

torre = Torre()
while torre.vida > 0:
    print("\n1. Defender")
    print("2. Reparar")
    op = input("Elegí: ")
    if op == "1":
        torre.defender()
    elif op == "2":
        torre.reparar()
    torre.recibir_ataque()
    print("Vida actual:", torre.vida)

print("La torre cayó")
print("GAME OVER")