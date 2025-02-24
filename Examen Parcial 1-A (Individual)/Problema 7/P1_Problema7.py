class Nodo:
    """
    Clase que representa un nodo en la lista simplemente enlazada.
    """

    def __init__(self, valor):
        self.valor = valor  # Valor almacenado en el nodo
        self.siguiente = None  # Referencia al siguiente nodo


class ListaEnlazada:
    """
    Clase que implementa una lista simplemente enlazada.
    """

    def __init__(self):
        self.cabeza = None  # Inicialmente, la lista está vacía

    def insertar_al_inicio(self, valor):
        """
        Inserta un nuevo nodo al inicio de la lista.

        :param valor: El valor del nuevo nodo a insertar.
        """
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"Nodo con valor {valor} insertado al inicio.")

    def insertar_al_final(self, valor):
        """
        Inserta un nuevo nodo al final de la lista.

        :param valor: El valor del nuevo nodo a insertar.
        """
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorremos hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Nodo con valor {valor} insertado al final.")

    def buscar(self, valor):
        """
        Busca un nodo por su valor.

        :param valor: El valor a buscar.
        :return: Nodo - El nodo encontrado, o None si no existe.
        """
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                print(f"Nodo con valor {valor} encontrado.")
                return actual
            actual = actual.siguiente
        print(f"Nodo con valor {valor} no encontrado.")
        return None

    def eliminar(self, valor):
        """
        Elimina un nodo por su valor.

        :param valor: El valor del nodo a eliminar.
        """
        if not self.cabeza:
            print("La lista está vacía, no se puede eliminar ningún nodo.")
            return

        # Caso especial: el nodo a eliminar es la cabeza
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            print(f"Nodo con valor {valor} eliminado (era la cabeza).")
            return

        # Buscar el nodo a eliminar
        anterior = None
        actual = self.cabeza
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente

        if not actual:  # No se encontró el nodo
            print(f"Nodo con valor {valor} no encontrado para eliminar.")
            return

        # Eliminar el nodo
        anterior.siguiente = actual.siguiente
        print(f"Nodo con valor {valor} eliminado.")

    def mostrar_lista(self):
        """
        Muestra los valores de todos los nodos en la lista.
        """
        if not self.cabeza:
            print("La lista está vacía.")
            return

        print("Contenido de la lista:")
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> " if actual.siguiente else " -> None\n")
            actual = actual.siguiente


# Creamos una instancia de la lista
lista = ListaEnlazada()

# Insertar nodos
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_final(30)
lista.insertar_al_final(40)

# Mostrar lista
lista.mostrar_lista()

# Buscar nodos
lista.buscar(30)
lista.buscar(50)  # No existe

# Eliminar nodos
lista.eliminar(20)
lista.eliminar(50)  # No existe

# Mostrar lista actualizada
lista.mostrar_lista()