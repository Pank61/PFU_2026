# Ejercicio 89: Leer N numeros y contar cuantos son positivos, negativos y cero
# Usar: Para + Si

class Numeros:
    def __init__(self):
        self.positivos = 0
        self.negativos = 0
        self.ceros = 0

    def leer(self):
        n = int(input("Cuantos numeros va a ingresar: "))
        for i in range(n):
            numero = float(input("Ingrese un numero: "))
            if numero > 0:
                self.positivos = self.positivos + 1
            elif numero < 0:
                self.negativos = self.negativos + 1
            else:
                self.ceros = self.ceros + 1

    def mostrar(self):
        print("Positivos:", self.positivos)
        print("Negativos:", self.negativos)
        print("Ceros:", self.ceros)


numeros = Numeros()
numeros.leer()
numeros.mostrar()
