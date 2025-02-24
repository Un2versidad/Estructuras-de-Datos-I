class ColaConDosPilas:
    """
    Clase que implementa una cola utilizando dos pilas.
    """

    def __init__(self):
        self.pila_entrada = []  # Pila para manejar las operaciones de enqueue
        self.pila_salida = []  # Pila para manejar las operaciones de dequeue

    def enqueue(self, x):
        """
        Agrega un elemento a la cola.

        :param x: El elemento a agregar.
        """
        self.pila_entrada.append(x)
        print(f"Elemento {x} agregado a la cola.")

    def dequeue(self):
        """
        Elimina y devuelve el elemento en la parte frontal de la cola.

        :return: El elemento eliminado, o None si la cola está vacía.
        """
        if not self.pila_salida and not self.pila_entrada:
            print("La cola está vacía. No se puede eliminar ningún elemento.")
            return None
        # Si la pila de salida está vacía, transferimos elementos de la pila de entrada
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        elemento = self.pila_salida.pop()
        print(f"Elemento {elemento} eliminado de la cola.")
        return elemento

    def front(self):
        """
        Obtiene el elemento en la parte frontal de la cola sin eliminarlo.

        :return: El elemento en la parte frontal, o None si la cola está vacía.
        """
        if not self.pila_salida and not self.pila_entrada:
            print("La cola está vacía. No hay elemento en la parte frontal.")
            return None
        # Si la pila de salida está vacía, transferimos elementos de la pila de entrada
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        print(f"Elemento en la parte frontal: {self.pila_salida[-1]}")
        return self.pila_salida[-1]

    def mostrar_cola(self):
        """
        Muestra los elementos de la cola.
        """
        if not self.pila_salida and not self.pila_entrada:
            print("La cola está vacía.")
            return
        print("Contenido de la cola (de frente a final):")
        for elemento in reversed(self.pila_salida):
            print(elemento)
        for elemento in self.pila_entrada:
            print(elemento)


# Crear una instancia de la cola con dos pilas
cola = ColaConDosPilas()

# Operaciones enqueue
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

# Mostrar cola
print("\nCola después de enqueue:")
cola.mostrar_cola()

# Operación front
cola.front()

# Operaciones dequeue
cola.dequeue()
cola.dequeue()

# Mostrar cola actualizada
print("\nCola después de dequeue:")
cola.mostrar_cola()

# Intentar hacer dequeue cuando la cola está vacía
cola.dequeue()
cola.dequeue()