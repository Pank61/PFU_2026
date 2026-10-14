# Ejercicio 91: Calculadora que permita realizar operaciones hasta seleccionar Salir
# Usar: Repetir + Segun

class Calculadora:
    def iniciar(self):
        while True:
            print("")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            opcion = int(input("Elija una opcion: "))

            if opcion == 5:
                print("Fin del programa")
                break

            if opcion >= 1 and opcion <= 4:
                a = float(input("Primer numero: "))
                b = float(input("Segundo numero: "))

                # Segun la opcion
                if opcion == 1:
                    print("Resultado:", a + b)
                elif opcion == 2:
                    print("Resultado:", a - b)
                elif opcion == 3:
                    print("Resultado:", a * b)
                elif opcion == 4:
                    if b == 0:
                        print("No se puede dividir entre 0")
                    else:
                        print("Resultado:", a / b)
            else:
                print("Opcion no valida")


calculadora = Calculadora()
calculadora.iniciar()
