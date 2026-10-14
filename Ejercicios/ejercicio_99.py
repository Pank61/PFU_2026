# Ejercicio 99: Leer N edades y determinar cuantas corresponden a
# ninos, adolescentes, adultos y adultos mayores
# Usar: Para + Si
# ninos: 0 a 11 | adolescentes: 12 a 17 | adultos: 18 a 59 | adultos mayores: 60 o mas

class Edades:
    def __init__(self):
        self.ninos = 0
        self.adolescentes = 0
        self.adultos = 0
        self.mayores = 0

    def leer(self):
        n = int(input("Cuantas edades va a ingresar: "))
        for i in range(n):
            edad = int(input("Ingrese una edad: "))
            if edad <= 11:
                self.ninos = self.ninos + 1
            elif edad <= 17:
                self.adolescentes = self.adolescentes + 1
            elif edad <= 59:
                self.adultos = self.adultos + 1
            else:
                self.mayores = self.mayores + 1

    def mostrar(self):
        print("Ninos:", self.ninos)
        print("Adolescentes:", self.adolescentes)
        print("Adultos:", self.adultos)
        print("Adultos mayores:", self.mayores)


edades = Edades()
edades.leer()
edades.mostrar()
