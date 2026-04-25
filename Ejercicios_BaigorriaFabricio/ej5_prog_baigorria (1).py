class Agenda:
    def __init__(self):
        self.nombres = []
        self.telefonos = []
        self.emails = []

    def añadir(self):
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        email = input("Email: ")

        self.nombres.append(nombre)
        self.telefonos.append(telefono)
        self.emails.append(email)

    def listar(self):
        for i in range(len(self.nombres)):
            print("Nombre:", self.nombres[i])
            print("Telefono:", self.telefonos[i])
            print("Email:", self.emails[i])
            print("-----")

    def buscar(self):
        nombre = input("Nombre a buscar: ")
        for i in range(len(self.nombres)):
            if self.nombres[i] == nombre:
                print("Telefono:", self.telefonos[i])
                print("Email:", self.emails[i])

    def editar(self):
        nombre = input("Nombre a editar: ")
        for i in range(len(self.nombres)):
            if self.nombres[i] == nombre:
                self.telefonos[i] = input("Nuevo telefono: ")
                self.emails[i] = input("Nuevo email: ")

    def menu(self):
        opcion = 0
        while opcion != 5:
            print("\n1 Añadir")
            print("2 Listar")
            print("3 Buscar")
            print("4 Editar")
            print("5 Salir")

            opcion = int(input("Opcion: "))

            if opcion == 1:
                self.añadir()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.buscar()
            elif opcion == 4:
                self.editar()


agenda = Agenda()
agenda.menu()