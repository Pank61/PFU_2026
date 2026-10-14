# Ejercicio 92: Menu de figuras geometricas y calcular areas repetidamente
# Usar: Repetir + Segun + Si

class Figuras:
    def iniciar(self):
        while True:
            print("")
            print("1. Cuadrado")
            print("2. Rectangulo")
            print("3. Triangulo")
            print("4. Circulo")
            print("5. Salir")
            opcion = int(input("Elija una opcion: "))

            # Segun la opcion
            if opcion == 1:
                lado = float(input("Ingrese el lado: "))
                if lado > 0:
                    print("Area:", lado * lado)
                else:
                    print("El lado debe ser mayor a 0")
            elif opcion == 2:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                if base > 0 and altura > 0:
                    print("Area:", base * altura)
                else:
                    print("Los datos deben ser mayores a 0")
            elif opcion == 3:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                if base > 0 and altura > 0:
                    print("Area:", base * altura / 2)
                else:
                    print("Los datos deben ser mayores a 0")
            elif opcion == 4:
                radio = float(input("Ingrese el radio: "))
                if radio > 0:
                    print("Area:", 3.1416 * radio * radio)
                else:
                    print("El radio debe ser mayor a 0")
            elif opcion == 5:
                print("Fin del programa")
                break
            else:
                print("Opcion no valida")


figuras = Figuras()
figuras.iniciar()
