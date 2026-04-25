class calculadora:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    def suma(self):
        print("Suma:", self.a + self.b)
        
    def resta(self):
        print("Resta:", self.a - self.b)
        
    def multiplicacion(self):
        print("Multiplicacion:", self.a * self.b)
        
    def division(self):
        if self.b != 0:
            print("Division:", self.a / self.b)
        else:
            print("No se puede dividir por cero")

calc=calculadora(10,5)
calc.suma()
calc.resta()
calc.multiplicacion()
calc.division()