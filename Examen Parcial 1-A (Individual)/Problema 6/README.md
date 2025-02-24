![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 6: Manejo de Inventario de Productos**

## **📖 Descripción del Problema**
Implementa una estructura para manejar un inventario de productos con los 
siguientes campos: ID, nombre, cantidad y precio. Escribe un programa que 
permita agregar, modificar y eliminar productos del inventario.

- **ID**: Identificador único del producto.
- **Nombre**: Nombre del producto.
- **Cantidad**: Cantidad disponible en el inventario.
- **Precio**: Precio del producto.

El programa debe permitir:
1. Agregar productos al inventario.
2. Modificar productos existentes.
3. Eliminar productos del inventario.
4. Mostrar todos los productos en el inventario.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `Producto`**:
   - Representa un producto con atributos: `nombre`, `cantidad` y `precio`.
   - Se utiliza un constructor (`__init__`) para inicializar estos atributos.

2. **Clase `Inventario`**:
   - Utiliza un **diccionario** para almacenar los productos, donde las claves son los IDs de los productos y los valores son objetos de la clase `Producto`.

### **💻 Explicación del Código**
El código implementa las siguientes operaciones:

1. **📝 Agregar Producto**:
   - Verifica si el ID del producto ya existe en el inventario.
   - Si no existe, agrega el producto al diccionario.

2. **🔄 Modificar Producto**:
   - Busca el producto por su ID.
   - Permite modificar uno o varios atributos del producto (nombre, cantidad, precio).

3. **❌ Eliminar Producto**:
   - Busca el producto por su ID.
   - Si existe, lo elimina del diccionario.

4. **📊 Mostrar Inventario**:
   - Itera sobre el diccionario e imprime los detalles de cada producto.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Datos Iniciales**
| ID    | Nombre      | Cantidad | Precio |
|-------|-------------|----------|--------|
| P001  | Laptop      | 10       | 1500.0 |
| P002  | Smartphone  | 50       | 800.0  |
| P003  | Tablet      | 20       | 450.0  |

#### **Operaciones**
1. **Agregar Producto**:
   - Agregamos tres productos iniciales.

2. **Mostrar Inventario**:
   ```
   Inventario:
   ID: P001, Nombre: Laptop, Cantidad: 10, Precio: $1500.00
   ID: P002, Nombre: Smartphone, Cantidad: 50, Precio: $800.00
   ID: P003, Nombre: Tablet, Cantidad: 20, Precio: $450.00
   ```

3. **Modificar Producto**:
   - Modificamos el producto con ID `P002`:
     - Nueva cantidad: 45
     - Nuevo precio: 750.0

4. **Eliminar Producto**:
   - Eliminamos el producto con ID `P003`.

5. **Mostrar Inventario Actualizado**:
   ```
   Inventario:
   ID: P001, Nombre: Laptop, Cantidad: 10, Precio: $1500.00
   ID: P002, Nombre: Smartphone, Cantidad: 45, Precio: $750.00
   ```

### **⏱️ Complejidad Temporal**
1. **Agregar Producto**:
   - Complejidad: O(1), ya que el acceso y la inserción en un diccionario tienen tiempo constante.

2. **Modificar Producto**:
   - Complejidad: O(1), ya que el acceso y la modificación en un diccionario tienen tiempo constante.

3. **Eliminar Producto**:
   - Complejidad: O(1), ya que la eliminación en un diccionario tiene tiempo constante.

4. **Mostrar Inventario**:
   - Complejidad: O(N), donde N es el número de productos en el inventario, ya que se recorre todo el diccionario.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza un **diccionario** para almacenar los productos, lo cual permite acceso rápido por ID.
   - Cada producto se representa mediante una **clase tradicional** (`Producto`), que es una estructura de registro.

2. **Por Qué Se Usó un Diccionario**:
   - Los diccionarios son ideales para este problema porque permiten acceder, modificar y eliminar elementos de manera eficiente utilizando claves únicas (IDs).

3. **Eficiencia**:
   - Complejidad temporal: O(1) para agregar, modificar y eliminar productos; O(N) para mostrar el inventario.
   - Complejidad espacial: O(N), donde N es el número de productos en el inventario.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Producto 'Laptop' agregado al inventario.
Producto 'Smartphone' agregado al inventario.
Producto 'Tablet' agregado al inventario.
Inventario:
ID: P001, Nombre: Laptop, Cantidad: 10, Precio: $1500.00
ID: P002, Nombre: Smartphone, Cantidad: 50, Precio: $800.00
ID: P003, Nombre: Tablet, Cantidad: 20, Precio: $450.00
Producto con ID P002 modificado exitosamente.
Producto 'Tablet' eliminado del inventario.
Inventario:
ID: P001, Nombre: Laptop, Cantidad: 10, Precio: $1500.00
ID: P002, Nombre: Smartphone, Cantidad: 45, Precio: $750.00
```
