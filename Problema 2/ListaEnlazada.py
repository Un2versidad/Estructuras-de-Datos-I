# Lista Enlazada

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
      nuevo_nodo = Nodo(valor)
      if self.cabeza is None:
        self.cabeza = nuevo_nodo
      else:
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo
    
    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end="->")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def buscar(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

lista.mostrar() #1->2->3->4

#buscar valor
print(lista.buscar(2))
print(lista.buscar(4))
print(lista.buscar(5))