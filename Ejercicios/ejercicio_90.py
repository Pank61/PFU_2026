# Ejercicio 90: Mostrar la tabla de multiplicar de un numero
# y permitir repetir el proceso con otros numeros
# Usar: Repetir + Para

class Tabla:
    def mostrar_tabla(self, numero):
        for i in range(1, 11):
            print(numero, "x", i, "=", numero * i)

    def iniciar(self):
        while True:
            numero = int(input("Ingrese un numero: "))
            self.mostrar_tabla(numero)
            respuesta = input("Desea repetir con otro numero? (s/n): ")
            if respuesta == "n":
                break


tabla = Tabla()
tabla.iniciar()
