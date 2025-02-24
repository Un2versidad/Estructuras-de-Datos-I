![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 11: Implementación de una Cola con un Arreglo Dinámico**

## **📖 Descripción del Problema**
Implementar una cola utilizando un arreglo dinámico que permita realizar las siguientes operaciones:
1. **`enqueue(x)`**: Agregar un elemento al final de la cola.
2. **`dequeue()`**: Eliminar el elemento en la parte frontal de la cola.
3. **`front()`**: Obtener el elemento en la parte frontal de la cola sin eliminarlo.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `Cola`**:
   - Implementa una cola utilizando un **arreglo dinámico** (`list` en Python).
   - Contiene métodos para realizar las operaciones `enqueue`, `dequeue`, `front` y mostrar el contenido de la cola.

### **💻 Explicación del Código**

#### **Clase `Cola`**
- **Constructor (`__init__`)**:
  - Inicializa un arreglo vacío (`self.arreglo`) para almacenar los elementos de la cola.

- **Método `enqueue(x)`**:
  - Agrega un elemento al final del arreglo, que representa el extremo trasero de la cola.
  - Complejidad: O(1) en promedio, ya que `append` es eficiente en Python.

- **Método `dequeue()`**:
  - Elimina y devuelve el primer elemento del arreglo, que representa el extremo frontal de la cola.
  - Si la cola está vacía, imprime un mensaje y devuelve `None`.
  - Complejidad: O(N), donde N es el número de elementos en la cola, ya que `pop(0)` requiere desplazar todos los elementos restantes.

- **Método `front()`**:
  - Devuelve el primer elemento del arreglo sin eliminarlo.
  - Si la cola está vacía, imprime un mensaje y devuelve `None`.
  - Complejidad: O(1), ya que acceder al primer elemento de un arreglo es directo.

- **Método `mostrar_cola()`**:
  - Recorre el arreglo e imprime los elementos en orden (de frente a final).
  - Complejidad: O(N), donde N es el número de elementos en la cola.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Operaciones Realizadas**
1. **Enqueue**:
   - Insertamos elementos `10`, `20` y `30`.
   - Resultado: `[10, 20, 30]` (el frente es `10`).

2. **Mostrar Cola**:
   ```
   Contenido de la cola (de frente a final):
   10
   20
   30
   ```

3. **Front**:
   - Obtenemos el elemento en el frente: `10`.

4. **Dequeue**:
   - Eliminamos el elemento en el frente (`10`).
   - Resultado: `[20, 30]` (el frente es `20`).
   - Eliminamos el siguiente elemento en el frente (`20`).
   - Resultado: `[30]` (el frente es `30`).

5. **Mostrar Cola Actualizada**:
   ```
   Contenido de la cola (de frente a final):
   30
   ```

6. **Dequeue en Cola Vacía**:
   - Intentamos eliminar un elemento cuando la cola está vacía.
   - Mensaje: "La cola está vacía. No se puede eliminar ningún elemento."

### **⏱️ Complejidad Temporal**
1. **Enqueue**:
   - Complejidad: O(1) en promedio, ya que `append` es eficiente en Python.

2. **Dequeue**:
   - Complejidad: O(N), donde N es el número de elementos en la cola, ya que `pop(0)` requiere desplazar todos los elementos restantes.

3. **Front**:
   - Complejidad: O(1), ya que acceder al primer elemento de un arreglo es directo.

4. **Mostrar Cola**:
   - Complejidad: O(N), donde N es el número de elementos en la cola.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza un **arreglo dinámico** (`list` en Python) para implementar la cola.
   - Las operaciones `enqueue`, `dequeue` y `front` son compatibles con esta estructura.

2. **Por Qué Se Usó un Arreglo Dinámico**:
   - Los arreglos dinámicos son ideales para este problema porque permiten inserciones eficientes al final (`enqueue`) y acceso directo al frente (`front`).
   - Sin embargo, `dequeue` tiene una complejidad lineal debido a la necesidad de desplazar elementos.

3. **Eficiencia**:
   - Complejidad temporal: O(1) para `enqueue` y `front`; O(N) para `dequeue` y mostrar la cola.
   - Complejidad espacial: O(N), donde N es el número de elementos en la cola.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Elemento 10 agregado a la cola.
Elemento 20 agregado a la cola.
Elemento 30 agregado a la cola.
Cola después de enqueue:
Contenido de la cola (de frente a final):
10
20
30
Elemento en la parte frontal: 10
Elemento 10 eliminado de la cola.
Elemento 20 eliminado de la cola.
Cola después de dequeue:
Contenido de la cola (de frente a final):
30
Elemento 30 eliminado de la cola.
La cola está vacía. No se puede eliminar ningún elemento.
```
