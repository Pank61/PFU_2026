# Ejercicio 93: Solicitar notas de estudiantes hasta finalizar
# y calcular el promedio, la nota mayor y la nota menor
# Usar: Mientras + Si

class Estudiantes:
    def __init__(self):
        self.suma = 0
        self.cantidad = 0
        self.mayor = 0
        self.menor = 100

    def leer_notas(self):
        print("Para finalizar escriba -1")
        nota = float(input("Ingrese una nota: "))
        while nota != -1:
            self.suma = self.suma + nota
            self.cantidad = self.cantidad + 1
            if nota > self.mayor:
                self.mayor = nota
            if nota < self.menor:
                self.menor = nota
            nota = float(input("Ingrese una nota: "))

    def mostrar(self):
        if self.cantidad > 0:
            promedio = self.suma / self.cantidad
            print("Promedio:", promedio)
            print("Nota mayor:", self.mayor)
            print("Nota menor:", self.menor)
        else:
            print("No se ingresaron notas")


estudiantes = Estudiantes()
estudiantes.leer_notas()
estudiantes.mostrar()
