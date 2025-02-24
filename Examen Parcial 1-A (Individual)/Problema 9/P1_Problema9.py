# Definimos una clase para implementar una pila utilizando un arreglo dinámico
class Pila:
    def __init__(self):
        self.arreglo = []  # Arreglo dinámico para almacenar los elementos

    def push(self, x):
        """
        Agrega un elemento al tope de la pila.

        :param x: El elemento a agregar.
        """
        self.arreglo.append(x)
        print(f"Elemento {x} agregado a la pila.")

    def pop(self):
        """
        Elimina el elemento en el tope de la pila.

        :return: El elemento eliminado, o None si la pila está vacía.
        """
        if not self.arreglo:
            print("La pila está vacía. No se puede eliminar ningún elemento.")
            return None
        elemento = self.arreglo.pop()
        print(f"Elemento {elemento} eliminado de la pila.")
        return elemento

    def top(self):
        """
        Obtiene el elemento en el tope de la pila sin eliminarlo.

        :return: El elemento en el tope, o None si la pila está vacía.
        """
        if not self.arreglo:
            print("La pila está vacía. No hay elemento en el tope.")
            return None
        print(f"Elemento en el tope: {self.arreglo[-1]}")
        return self.arreglo[-1]

    def mostrar_pila(self):
        """
        Muestra los elementos de la pila.
        """
        if not self.arreglo:
            print("La pila está vacía.")
            return
        print("Contenido de la pila (de tope a base):")
        for i in range(len(self.arreglo) - 1, -1, -1):
            print(self.arreglo[i])


# Crear una instancia de la pila
pila = Pila()

# Operaciones push
pila.push(10)
pila.push(20)
pila.push(30)

# Mostrar pila
print("\nPila después de push:")
pila.mostrar_pila()

# Operación top
pila.top()

# Operaciones pop
pila.pop()
pila.pop()

# Mostrar pila actualizada
print("\nPila después de pop:")
pila.mostrar_pila()

# Intentar hacer pop cuando la pila está vacía
pila.pop()
pila.pop()