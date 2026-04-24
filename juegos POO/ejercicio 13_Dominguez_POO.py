import random
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def tirar(self):
        dado = random.randint(1, 6)
        self.puntos += dado
        print(f"{self.nombre} sacó {dado}")

jugador = Jugador("Jugador")
bot = Jugador("BOT")
rondas = 5
for i in range(rondas):
    print(f"\n--- RONDA {i+1} ---")
    input("Presioná Enter para tirar")

    jugador.tirar()
    bot.tirar()
    print(f"Puntaje -> Jugador:{jugador.puntos} BOT:{bot.puntos}")

print("\nRESULTADO FINAL")
if jugador.puntos > bot.puntos:
    print("GANASTE")
elif jugador.puntos < bot.puntos:
    print("PERDISTE")
else:
    print("EMPATE")

print("GAME OVER")