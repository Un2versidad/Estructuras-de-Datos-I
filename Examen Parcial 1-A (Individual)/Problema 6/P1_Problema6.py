# Definimos una clase para representar un producto
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

# Definimos una clase para manejar el inventario
class Inventario:
    def __init__(self):
        # Diccionario para almacenar productos por ID
        self.inventario = {}

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.inventario:
            print(f"El producto con ID {id_producto} ya existe en el inventario.")
        else:
            self.inventario[id_producto] = Producto(nombre, cantidad, precio)
            print(f"Producto '{nombre}' agregado al inventario.")

    def modificar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto not in self.inventario:
            print(f"El producto con ID {id_producto} no existe en el inventario.")
            return

        producto = self.inventario[id_producto]
        if nombre is not None:
            producto.nombre = nombre
        if cantidad is not None:
            producto.cantidad = cantidad
        if precio is not None:
            producto.precio = precio

        print(f"Producto con ID {id_producto} modificado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto not in self.inventario:
            print(f"El producto con ID {id_producto} no existe en el inventario.")
        else:
            producto_eliminado = self.inventario.pop(id_producto)
            print(f"Producto '{producto_eliminado.nombre}' eliminado del inventario.")

    def mostrar_inventario(self):
        if not self.inventario:
            print("El inventario está vacío.")
            return

        print("\nInventario:")
        for id_producto, producto in self.inventario.items():
            print(f"ID: {id_producto}, Nombre: {producto.nombre}, "
                  f"Cantidad: {producto.cantidad}, Precio: ${producto.precio:.2f}")

# Creamos una instancia del inventario
inventario = Inventario()

# Agregar productos
inventario.agregar_producto("P001", "Laptop", 10, 1500.0)
inventario.agregar_producto("P002", "Smartphone", 50, 800.0)
inventario.agregar_producto("P003", "Tablet", 20, 450.0)

# Mostrar inventario
inventario.mostrar_inventario()

# Modificar un producto
inventario.modificar_producto("P002", cantidad=45, precio=750.0)

# Eliminar un producto
inventario.eliminar_producto("P003")

# Mostrar inventario actualizado
inventario.mostrar_inventario()