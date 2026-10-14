# Ejercicio 97: Menu bancario para consultar saldo, depositar, retirar y salir
# Se valida que haya fondos suficientes
# Usar: Repetir + Segun + Si

class Banco:
    def __init__(self):
        self.saldo = 1000

    def consultar(self):
        print("Su saldo es:", self.saldo)

    def depositar(self):
        monto = float(input("Monto a depositar: "))
        if monto > 0:
            self.saldo = self.saldo + monto
            print("Deposito realizado")
        else:
            print("El monto debe ser mayor a 0")

    def retirar(self):
        monto = float(input("Monto a retirar: "))
        if monto > self.saldo:
            print("Fondos insuficientes")
        elif monto <= 0:
            print("El monto debe ser mayor a 0")
        else:
            self.saldo = self.saldo - monto
            print("Retiro realizado")

    def iniciar(self):
        while True:
            print("")
            print("1. Consultar saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Salir")
            opcion = int(input("Elija una opcion: "))

            # Segun la opcion
            if opcion == 1:
                self.consultar()
            elif opcion == 2:
                self.depositar()
            elif opcion == 3:
                self.retirar()
            elif opcion == 4:
                print("Gracias por usar el banco")
                break
            else:
                print("Opcion no valida")


banco = Banco()
banco.iniciar()
