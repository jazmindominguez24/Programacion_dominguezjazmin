class Alumno:
    def cargar(self):
        self.nombre = input("Nombre del alumno: ")
        self.nota = float(input("Nota: "))
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    def resultado(self):
        if self.nota >= 6:
            print("Aprobado")
        else:
            print("Desaprobado")

alumno1 = Alumno()
alumno1.cargar()
alumno1.mostrar()
alumno1.resultado()