# Ejercicio 100: Menu para factorial, tabla de multiplicar, paridad y cuadrado
# Repetir hasta seleccionar Salir
# Usar: Repetir + Segun + Si

class Menu:
    def factorial(self, n):
        if n < 0:
            print("No existe el factorial de un numero negativo")
        else:
            resultado = 1
            for i in range(1, n + 1):
                resultado = resultado * i
            print("El factorial es:", resultado)

    def tabla(self, n):
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

    def paridad(self, n):
        if n % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")

    def cuadrado(self, n):
        print("El cuadrado es:", n * n)

    def iniciar(self):
        while True:
            print("")
            print("1. Factorial")
            print("2. Tabla de multiplicar")
            print("3. Paridad")
            print("4. Cuadrado")
            print("5. Salir")
            opcion = int(input("Elija una opcion: "))

            if opcion == 5:
                print("Fin del programa")
                break

            if opcion >= 1 and opcion <= 4:
                n = int(input("Ingrese un numero: "))

                # Segun la opcion
                if opcion == 1:
                    self.factorial(n)
                elif opcion == 2:
                    self.tabla(n)
                elif opcion == 3:
                    self.paridad(n)
                elif opcion == 4:
                    self.cuadrado(n)
            else:
                print("Opcion no valida")


menu = Menu()
menu.iniciar()
