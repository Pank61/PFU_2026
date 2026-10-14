# Ejercicio 98: Ingresar 10 notas, clasificar aprobadas/reprobadas
# y mostrar estadisticas (nota de 0 a 100, se aprueba con 51)
# Usar: Para + Si

class Notas:
    def __init__(self):
        self.aprobadas = 0
        self.reprobadas = 0
        self.suma = 0
        self.mayor = 0
        self.menor = 100

    def leer(self):
        for i in range(10):
            nota = float(input("Ingrese la nota: "))
            self.suma = self.suma + nota

            if nota >= 51:
                self.aprobadas = self.aprobadas + 1
            else:
                self.reprobadas = self.reprobadas + 1

            if nota > self.mayor:
                self.mayor = nota
            if nota < self.menor:
                self.menor = nota

    def mostrar(self):
        print("Aprobadas:", self.aprobadas)
        print("Reprobadas:", self.reprobadas)
        print("Promedio:", self.suma / 10)
        print("Nota mayor:", self.mayor)
        print("Nota menor:", self.menor)


notas = Notas()
notas.leer()
notas.mostrar()
