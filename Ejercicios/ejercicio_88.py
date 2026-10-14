# Ejercicio 88: Leer N numeros y calcular la suma y el promedio
# Usar: Para + acumulador

class Numeros:
    def __init__(self):
        self.suma = 0
        self.promedio = 0

    def leer(self):
        n = int(input("Cuantos numeros va a ingresar: "))
        for i in range(n):
            numero = float(input("Ingrese un numero: "))
            self.suma = self.suma + numero    # acumulador
        self.promedio = self.suma / n

    def mostrar(self):
        print("La suma es:", self.suma)
        print("El promedio es:", self.promedio)


numeros = Numeros()
numeros.leer()
numeros.mostrar()
