# Definimos una clase para implementar una cola utilizando un arreglo dinámico
class Cola:
    def __init__(self):
        self.arreglo = []  # Arreglo dinámico para almacenar los elementos

    def enqueue(self, x):
        """
        Agrega un elemento al final de la cola.

        :param x: El elemento a agregar.
        """
        self.arreglo.append(x)
        print(f"Elemento {x} agregado a la cola.")

    def dequeue(self):
        """
        Elimina el elemento en la parte frontal de la cola.

        :return: El elemento eliminado, o None si la cola está vacía.
        """
        if not self.arreglo:
            print("La cola está vacía. No se puede eliminar ningún elemento.")
            return None
        elemento = self.arreglo.pop(0)  # Elimina el primer elemento
        print(f"Elemento {elemento} eliminado de la cola.")
        return elemento

    def front(self):
        """
        Obtiene el elemento en la parte frontal de la cola sin eliminarlo.

        :return: El elemento en la parte frontal, o None si la cola está vacía.
        """
        if not self.arreglo:
            print("La cola está vacía. No hay elemento en la parte frontal.")
            return None
        print(f"Elemento en la parte frontal: {self.arreglo[0]}")
        return self.arreglo[0]

    def mostrar_cola(self):
        """
        Muestra los elementos de la cola.
        """
        if not self.arreglo:
            print("La cola está vacía.")
            return
        print("Contenido de la cola (de frente a final):")
        for elemento in self.arreglo:
            print(elemento)


# Crear una instancia de la cola
cola = Cola()

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