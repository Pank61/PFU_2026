# Ejercicio 95: Leer numeros hasta 0 y determinar
# cuantos son pares, impares, positivos y negativos
# Usar: Mientras + operadores

class Numeros:
    def __init__(self):
        self.pares = 0
        self.impares = 0
        self.positivos = 0
        self.negativos = 0

    def leer(self):
        print("Para terminar escriba 0")
        n = int(input("Ingrese un numero: "))
        while n != 0:
            if n % 2 == 0:
                self.pares = self.pares + 1
            else:
                self.impares = self.impares + 1

            if n > 0:
                self.positivos = self.positivos + 1
            else:
                self.negativos = self.negativos + 1

            n = int(input("Ingrese un numero: "))

    def mostrar(self):
        print("Pares:", self.pares)
        print("Impares:", self.impares)
        print("Positivos:", self.positivos)
        print("Negativos:", self.negativos)


numeros = Numeros()
numeros.leer()
numeros.mostrar()
