# Ejercicio 86: Leer 10 numeros y contar cuantos son pares e impares
# Usar: Para + Si

class Numeros:
    def __init__(self):
        self.pares = 0
        self.impares = 0

    def leer(self):
        for i in range(10):
            n = int(input("Ingrese un numero: "))
            if n % 2 == 0:
                self.pares = self.pares + 1
            else:
                self.impares = self.impares + 1

    def mostrar(self):
        print("Cantidad de pares:", self.pares)
        print("Cantidad de impares:", self.impares)


numeros = Numeros()
numeros.leer()
numeros.mostrar()
