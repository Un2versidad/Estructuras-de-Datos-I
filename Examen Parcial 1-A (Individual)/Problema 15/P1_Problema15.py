import heapq
from collections import deque

class SistemaEntrega:
    """
    Clase que implementa un sistema de entrega de pedidos con prioridades.
    """

    def __init__(self):
        # Cola de prioridad para los pedidos (usando un heap)
        self.pedidos = []  # (prioridad, id_pedido, descripcion)
        self.id_pedido_actual = 0  # Identificador único para cada pedido

        # Cola para los repartidores disponibles
        self.repartidores_disponibles = deque()

    def agregar_pedido(self, descripcion, es_urgente):
        """
        Agrega un nuevo pedido al sistema.

        :param descripcion: Str - Descripción del pedido.
        :param es_urgente: Bool - True si el pedido es urgente, False si es normal.
        """
        prioridad = 1 if es_urgente else 2  # Urgentes tienen prioridad más alta
        self.id_pedido_actual += 1
        pedido = (prioridad, self.id_pedido_actual, descripcion)
        heapq.heappush(self.pedidos, pedido)
        print(f"Pedido agregado: {descripcion} (Prioridad: {'Urgente' if es_urgente else 'Normal'})")

    def agregar_repartidor(self, nombre):
        """
        Agrega un repartidor al sistema.

        :param nombre: Str - Nombre del repartidor.
        """
        self.repartidores_disponibles.append(nombre)
        print(f"Repartidor '{nombre}' agregado al sistema.")

    def asignar_pedido(self):
        """
        Asigna el próximo pedido disponible a un repartidor libre.
        """
        if not self.repartidores_disponibles:
            print("No hay repartidores disponibles.")
            return
        if not self.pedidos:
            print("No hay pedidos pendientes.")
            return
        # Obtener el próximo pedido según la prioridad
        prioridad, id_pedido, descripcion = heapq.heappop(self.pedidos)
        repartidor = self.repartidores_disponibles.popleft()  # Asignar al primer repartidor disponible
        print(f"Pedido asignado: '{descripcion}' -> Repartidor: {repartidor}")

    def mostrar_pedidos_pendientes(self):
        """
        Muestra los pedidos pendientes en orden de prioridad.
        """
        if not self.pedidos:
            print("No hay pedidos pendientes.")
            return
        print("Pedidos pendientes (ordenados por prioridad):")
        for pedido in sorted(self.pedidos):
            prioridad, id_pedido, descripcion = pedido
            tipo = "Urgente" if prioridad == 1 else "Normal"
            print(f"- ID: {id_pedido}, Descripción: {descripcion}, Tipo: {tipo}")


# Crear una instancia del sistema de entrega
sistema = SistemaEntrega()

# Agregar pedidos
sistema.agregar_pedido("Entregar paquete a Juan", es_urgente=True)
sistema.agregar_pedido("Entregar comida a María", es_urgente=False)
sistema.agregar_pedido("Entregar documentos a Carlos", es_urgente=True)

# Agregar repartidores
sistema.agregar_repartidor("Repartidor A")
sistema.agregar_repartidor("Repartidor B")

# Mostrar pedidos pendientes
print("\nMostrar pedidos pendientes:")
sistema.mostrar_pedidos_pendientes()

# Asignar pedidos a repartidores
print("\nAsignar pedidos:")
sistema.asignar_pedido()
sistema.asignar_pedido()

# Mostrar pedidos pendientes después de asignar
print("\nMostrar pedidos pendientes después de asignar:")
sistema.mostrar_pedidos_pendientes()

# Intentar asignar cuando no hay repartidores disponibles
sistema.asignar_pedido()