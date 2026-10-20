class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if len(self.items) == 0:
            print("La pila está vacía")
            return None
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if len(self.items) == 0:
            print("La cola está vacía")
            return None
        return self.items.pop(0)


# Reto individual: verificar que la cola retire primero L01
lista = ListaEnlazada()
cola = Cola()

# Datos de prueba: se registran en la lista enlazada y se encolan
lista.agregar("L01", "Python")
lista.agregar("L02", "Redes")
lista.agregar("L03", "Git")

cola.encolar("L01")
cola.encolar("L02")
cola.encolar("L03")

print("Lista enlazada:")
lista.mostrar()

primero = cola.desencolar()
print("Primer elemento que retira la cola:", primero)

if primero == "L01":
    print("Correcto: la cola retiró primero L01")
else:
    print("Error: la cola no retiró primero L01")
