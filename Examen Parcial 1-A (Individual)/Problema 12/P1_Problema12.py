from collections import deque

# Definimos una clase para simular un sistema de atención en una tienda utilizando una cola
class SistemaAtencion:
    def __init__(self):
        self.fila = deque()  # Cola para almacenar los clientes

    def agregar_cliente(self, nombre_cliente):
        """
        Agrega un cliente a la fila de atención.

        :param nombre_cliente: Str - Nombre del cliente a agregar.
        """
        self.fila.append(nombre_cliente)
        print(f"Cliente '{nombre_cliente}' agregado a la fila.")

    def atender_cliente(self):
        """
        Atiende al cliente en la parte frontal de la fila.

        :return: Str - Nombre del cliente atendido, o None si no hay clientes.
        """
        if not self.fila:
            print("No hay clientes en la fila.")
            return None

        cliente_atendido = self.fila.popleft()
        print(f"Cliente '{cliente_atendido}' ha sido atendido.")
        return cliente_atendido

    def mostrar_fila(self):
        """
        Muestra los clientes en la fila de atención.
        """
        if not self.fila:
            print("La fila está vacía.")
            return
        print("Clientes en la fila (de frente a final):")
        for cliente in self.fila:
            print(cliente)


# Crear una instancia del sistema de atención
sistema = SistemaAtencion()

# Agregar clientes a la fila
sistema.agregar_cliente("Juan Carlos")
sistema.agregar_cliente("María López")
sistema.agregar_cliente("Carlos Gómez")

# Mostrar la fila
print("\nEstado de la fila después de agregar clientes:")
sistema.mostrar_fila()

# Atender clientes
sistema.atender_cliente()
sistema.atender_cliente()

# Mostrar la fila actualizada
print("\nEstado de la fila después de atender clientes:")
sistema.mostrar_fila()

# Intentar atender cuando no hay clientes
sistema.atender_cliente()
sistema.atender_cliente()