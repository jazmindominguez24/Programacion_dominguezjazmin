class Calculadora:
    def __init__ (self,num1,num2):
        self.a=num1
        self.b=num2
        
    def sumar(self):
        print("SUMA",self.a + self.b)
        
    def restar(self):
        print("RESTAR",self.a - self.b)
        
    def dividir(self):
        if self.b!=0:
            print("DIVIDIR", self.a/self.b)
        else:
            print("no se puede dividir un numero por cero")
            
    def multiplicar(self):
        print("MULTIPLICACION", self.a * self.b)
calcu=Calculadora (23,5)
calcu.sumar()
calcu.restar()
calcu.dividir()
calcu.multiplicar()