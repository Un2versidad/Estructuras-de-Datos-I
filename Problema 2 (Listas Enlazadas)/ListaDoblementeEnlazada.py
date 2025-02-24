# Lista Doblemente Enlazada

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
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
        nuevo_nodo.anterior = nodo_actual

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end="->")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def agregarvalorentrenodos(self, valor, posicion):
        nuevo_nodo = Nodo(valor)
        if posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            if self.cabeza:
                self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            for i in range(posicion - 1):
                if nodo_actual.siguiente:
                    nodo_actual = nodo_actual.siguiente
                else:
                    print("Posición inválida")
                    return
            nuevo_nodo.siguiente = nodo_actual.siguiente
            if nodo_actual.siguiente:
                nodo_actual.siguiente.anterior = nuevo_nodo
              
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_actual           

    def buscar(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                return True
            nodo_actual = nodo_actual.siguiente
        return False
      
    def eliminar(self, valor):
        # Si la lista está vacía, no hay nada que eliminar
        if self.cabeza is None:
            print(f"La lista está vacía. No se puede eliminar el valor {valor}.")
            return False

        # Si el valor a eliminar es el primero de la lista
        if self.cabeza.valor == valor:
            print(f"El valor {valor} se ha eliminado de la lista.")
            self.cabeza = self.cabeza.siguiente
            return True
        # Si el valor a eliminar está en otra parte de la lista
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
          if nodo_actual.siguiente.valor == valor:
            nodo_actual.siguiente = nodo_actual.siguiente.siguiente
            print(f"El valor {valor} se ha eliminado de la lista.")
            return True

          nodo_actual = nodo_actual.siguiente

        print(f"El valor {valor} no se encuentra en la lista.")
        return False

lista = ListaDoblementeEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.mostrar() #1->2->3->4
#buscar valor
print(lista.buscar(2))
print(lista.buscar(4))
print(lista.buscar(5))

lista.agregarvalorentrenodos(int(input("Valor a Agregar: ")), int(input("Posicion: ")))
lista.mostrar()

eliminar = int(input("Ingrese el valor a eliminar: "))
lista.eliminar(eliminar)
lista.mostrar()
