# Definimos una clase para representar un nodo en la lista doblemente enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Valor almacenado en el nodo
        self.anterior = None  # Referencia al nodo anterior
        self.siguiente = None  # Referencia al siguiente nodo

# Definimos una clase para implementar la lista doblemente enlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista
        self.cola = None  # Último nodo de la lista

    def insertar_al_final(self, valor):
        """
        Inserta un nuevo nodo al final de la lista.

        :param valor: El valor del nuevo nodo a insertar.
        """
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

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
            print(actual.valor, end=" <-> " if actual.siguiente else " -> None\n")
            actual = actual.siguiente

    def invertir(self):
        """
        Invierte el orden de la lista doblemente enlazada.
        """
        if not self.cabeza or not self.cabeza.siguiente:
            # Si la lista está vacía o tiene solo un nodo, no hay nada que invertir
            return
        actual = self.cabeza

        # Intercambiamos las referencias 'anterior' y 'siguiente' de cada nodo
        while actual:
            temp = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temp
            actual = actual.anterior  # Avanzamos usando la referencia intercambiada
        # Al finalizar, intercambiamos las referencias de cabeza y cola
        temp = self.cabeza
        self.cabeza = self.cola
        self.cola = temp

# Crear una instancia de la lista doblemente enlazada
lista = ListaDoblementeEnlazada()

# Insertar nodos
lista.insertar_al_final(10)
lista.insertar_al_final(20)
lista.insertar_al_final(30)
lista.insertar_al_final(40)

# Mostrar lista original
print("Lista original:")
lista.mostrar_lista()

# Invertir la lista
lista.invertir()
print("\nLista invertida:")
lista.mostrar_lista()