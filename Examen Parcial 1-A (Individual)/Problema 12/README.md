![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 12: Simulación de un Sistema de Atención en una Tienda**

## **📖 Descripción del Problema**
Simula un sistema de atención en una tienda donde los clientes son atendidos en orden de llegada (FIFO). Implementa la cola para manejar la fila de clientes.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `SistemaAtencion`**:
   - Implementa un sistema de atención utilizando una **cola** (`deque` de Python).
   - Contiene métodos para realizar las operaciones:
     - `agregar_cliente`: Agregar un cliente a la fila.
     - `atender_cliente`: Atender al cliente en la parte frontal de la fila.
     - `mostrar_fila`: Mostrar los clientes en la fila.

2. **Cola (`deque`)**:
   - La biblioteca `collections.deque` es ideal para implementar colas debido a su eficiencia en inserciones y eliminaciones en ambos extremos.

### **💻 Explicación del Código**

#### **Clase `SistemaAtencion`**
- **Constructor (`__init__`)**:
  - Inicializa una cola vacía (`deque`) para almacenar los nombres de los clientes.

- **Método `agregar_cliente(nombre_cliente)`**:
  - Agrega un cliente al final de la cola utilizando el método `append`.
  - Complejidad: O(1), ya que `append` es eficiente en `deque`.

- **Método `atender_cliente()`**:
  - Elimina y devuelve el cliente en la parte frontal de la cola utilizando el método `popleft`.
  - Si la cola está vacía, imprime un mensaje y devuelve `None`.
  - Complejidad: O(1), ya que `popleft` es eficiente en `deque`.

- **Método `mostrar_fila()`**:
  - Recorre la cola e imprime los nombres de los clientes en orden (de frente a final).
  - Complejidad: O(N), donde N es el número de clientes en la cola.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Operaciones Realizadas**
1. **Agregar Clientes**:
   - Insertamos clientes: "Juan Carlos", "María López", "Carlos Gómez".
   - Resultado: `["Juan Carlos", "María López", "Carlos Gómez"]` (el frente es "Juan Carlos").

2. **Mostrar Fila**:
   ```
   Clientes en la fila (de frente a final):
   Juan Carlos
   María López
   Carlos Gómez
   ```

3. **Atender Clientes**:
   - Atendemos al cliente "Juan Carlos".
   - Atendemos al cliente "María López".
   - Resultado: `["Carlos Gómez"]` (el frente es "Carlos Gómez").

4. **Mostrar Fila Actualizada**:
   ```
   Clientes en la fila (de frente a final):
   Carlos Gómez
   ```

5. **Intentar Atender sin Clientes**:
   - Intentamos atender cuando la fila está vacía.
   - Mensaje: "No hay clientes en la fila."

---

### **⏱️ Complejidad Temporal**
1. **Agregar Cliente**:
   - Complejidad: O(1), ya que `append` es eficiente en `deque`.

2. **Atender Cliente**:
   - Complejidad: O(1), ya que `popleft` es eficiente en `deque`.

3. **Mostrar Fila**:
   - Complejidad: O(N), donde N es el número de clientes en la cola.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza una **cola** (`deque`) para implementar el sistema de atención.
   - Las operaciones `agregar_cliente`, `atender_cliente` y `mostrar_fila` son compatibles con esta estructura.

2. **Por Qué Se Usó una Cola (`deque`)**:
   - Las colas son ideales para este problema porque permiten manejar elementos en orden FIFO (primero en entrar, primero en salir).
   - `deque` es más eficiente que una lista estándar para operaciones como `append` y `popleft`.

3. **Eficiencia**:
   - Complejidad temporal: O(1) para agregar y atender clientes; O(N) para mostrar la fila.
   - Complejidad espacial: O(N), donde N es el número de clientes en la cola.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Cliente 'Juan Carlos' agregado a la fila.
Cliente 'María López' agregado a la fila.
Cliente 'Carlos Gómez' agregado a la fila.
Estado de la fila después de agregar clientes:
Clientes en la fila (de frente a final):
Juan Carlos
María López
Carlos Gómez
Cliente 'Juan Carlos' ha sido atendido.
Cliente 'María López' ha sido atendido.
Estado de la fila después de atender clientes:
Clientes en la fila (de frente a final):
Carlos Gómez
Cliente 'Carlos Gómez' ha sido atendido.
No hay clientes en la fila.
```
