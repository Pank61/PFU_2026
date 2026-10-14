# Ejercicio 94: Registrar edades hasta ingresar 0
# y determinar la cantidad de mayores y menores de edad
# Usar: Mientras + Si

class Edades:
    def __init__(self):
        self.mayores = 0
        self.menores = 0

    def leer(self):
        print("Para terminar escriba 0")
        edad = int(input("Ingrese una edad: "))
        while edad != 0:
            if edad >= 18:
                self.mayores = self.mayores + 1
            else:
                self.menores = self.menores + 1
            edad = int(input("Ingrese una edad: "))

    def mostrar(self):
        print("Mayores de edad:", self.mayores)
        print("Menores de edad:", self.menores)


edades = Edades()
edades.leer()
edades.mostrar()
