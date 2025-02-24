class Nodo:
    """
    Clase que representa un nodo en una lista enlazada.
    """
    def __init__(self, valor):
        self.valor = valor  # Valor almacenado en el nodo
        self.siguiente = None  # Referencia al siguiente nodo

def tiene_ciclo(cabeza):
    """
    Detecta si una lista enlazada tiene un ciclo utilizando el algoritmo de Floyd (tortuga y liebre).

    :param cabeza: Nodo - El primer nodo de la lista enlazada.
    :return: Bool - True si la lista tiene un ciclo, False en caso contrario.
    """
    if not cabeza or not cabeza.siguiente:
        # Si la lista está vacía o tiene un solo nodo, no puede haber ciclo
        return False
    tortuga = cabeza
    liebre = cabeza
    while liebre and liebre.siguiente:
        tortuga = tortuga.siguiente  # Avanza un paso
        liebre = liebre.siguiente.siguiente  # Avanza dos pasos
        if tortuga == liebre:
            # Si los punteros coinciden, hay un ciclo
            print("La lista tiene un ciclo.")
            return True
    # Si llegamos al final de la lista, no hay ciclo
    print("La lista no tiene un ciclo.")
    return False

# Crear una lista enlazada con un ciclo
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo2  # Crea un ciclo entre nodo4 y nodo2
# Detectar si hay un ciclo
tiene_ciclo(nodo1)

# Crear una lista enlazada sin ciclo
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo7 = Nodo(7)
nodo5.siguiente = nodo6
nodo6.siguiente = nodo7

# Detectar si hay un ciclo
tiene_ciclo(nodo5)