class Aventurero:
    def __init__(self):
        self.objetos = []

    def guardar(self, objeto):
        self.objetos.append(objeto)

    def usar(self):
        if len(self.objetos) > 0:
            usado = self.objetos.pop(0)
            print("Usaste:", usado)
        else:
            print("No hay objetos")

    def mostrar(self):
        print("Objetos:", self.objetos)


jugador = Aventurero()

acciones = 3

for i in range(acciones):
    print("1 Guardar")
    print("2 Usar")
    print("3 Ver inventario")

    op = input("Opcion: ")

    if op == "1":
        obj = input("Objeto: ")
        jugador.guardar(obj)
    elif op == "2":
        jugador.usar()
    elif op == "3":
        jugador.mostrar()

print("Juego terminado")