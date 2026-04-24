class Agenda:
    def cargar(self):
        self.contactos = []

    def añadir(self):
        nombre = input("Nombre: ")
        tel = input("Teléfono: ")
        email = input("Email: ")
        self.contactos.append([nombre, tel, email])

    def listar(self):
        for c in self.contactos:
            print(c)

    def buscar(self):
        nombre = input("Buscar nombre: ")
        for c in self.contactos:
            if c[0] == nombre:
                print("Encontrado:", c)

    def editar(self):
        nombre = input("Nombre a editar: ")
        for c in self.contactos:
            if c[0] == nombre:
                c[1] = input("Nuevo teléfono: ")
                c[2] = input("Nuevo email: ")


agenda = Agenda()
agenda.cargar()

print("\n 1-añadir 2-lista 3-buscar 4-editar 5-salir")
op=input("ingresa una opcion:")
while op!=5:
    if op=="1":
        self.añadir()
    if op=="2":
        self.mostrar()
    if op=="3":
        self.buscar()
    if op=="4":
        self.editar()
    if op=="5":
        print("cerrar menu..")
    op=input("ingresa una opcion:")