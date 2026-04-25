class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def mayor_edad(self):
        if self.edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor de edad")

persona1 = Persona("Fabricio", 20)
persona1.mostrar()
persona1.mayor_edad()