# Ejercicio 96: Ingresar productos y precios hasta seleccionar Finalizar
# y mostrar el total
# Usar: Repetir + Segun + acumulador

class Tienda:
    def __init__(self):
        self.total = 0

    def iniciar(self):
        while True:
            print("")
            print("1. Agregar producto")
            print("2. Finalizar")
            opcion = int(input("Elija una opcion: "))

            # Segun la opcion
            if opcion == 1:
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                self.total = self.total + precio    # acumulador
            elif opcion == 2:
                print("El total a pagar es:", self.total)
                break
            else:
                print("Opcion no valida")


tienda = Tienda()
tienda.iniciar()
