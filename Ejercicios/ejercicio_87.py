# Ejercicio 87: Leer 10 numeros y determinar el mayor y el menor
# Usar: Para + Si + Asignar

class Numeros:
    def __init__(self):
        self.mayor = 0
        self.menor = 0

    def leer(self):
        for i in range(10):
            n = int(input("Ingrese un numero: "))
            if i == 0:
                # el primer numero es el mayor y el menor por ahora
                self.mayor = n
                self.menor = n
            else:
                if n > self.mayor:
                    self.mayor = n
                if n < self.menor:
                    self.menor = n

    def mostrar(self):
        print("El mayor es:", self.mayor)
        print("El menor es:", self.menor)


numeros = Numeros()
numeros.leer()
numeros.mostrar()
