class Persona:
    def cargar(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        
    def mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
p = Persona()
p.cargar()
p.mostrar()
p.mayor_edad()