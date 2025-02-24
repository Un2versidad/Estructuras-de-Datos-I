![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 13: Implementación de una Cola con Dos Pilas**

## **📖 Descripción del Problema**
Implementa una cola con dos pilas. Es decir, simula el comportamiento de una cola utilizando únicamente dos pilas.

1. **`enqueue(x)`**: Agregar un elemento al final de la cola.
2. **`dequeue()`**: Eliminar el elemento en la parte frontal de la cola.
3. **`front()`**: Obtener el elemento en la parte frontal de la cola sin eliminarlo.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `ColaConDosPilas`**:
   - Implementa una cola utilizando dos pilas (`pila_entrada` y `pila_salida`).
   - Contiene métodos para realizar las operaciones `enqueue`, `dequeue`, `front` y mostrar el contenido de la cola.

2. **Pilas (`list`)**:
   - Se utilizan dos pilas para simular el comportamiento de una cola:
     - `pila_entrada`: Almacena los elementos agregados mediante `enqueue`.
     - `pila_salida`: Almacena los elementos transferidos desde `pila_entrada` para realizar `dequeue` y `front`.

### **💻 Explicación del Código**

#### **Clase `ColaConDosPilas`**
- **Constructor (`__init__`)**:
  - Inicializa dos pilas vacías:
    - `pila_entrada`: Para manejar las operaciones de `enqueue`.
    - `pila_salida`: Para manejar las operaciones de `dequeue` y `front`.

- **Método `enqueue(x)`**:
  - Agrega un elemento a `pila_entrada`.
  - Complejidad: O(1), ya que `append` es eficiente en Python.

- **Método `dequeue()`**:
  - Si `pila_salida` está vacía, transfiere todos los elementos de `pila_entrada` a `pila_salida` (invierte el orden).
  - Elimina y devuelve el elemento en el tope de `pila_salida`.
  - Si ambas pilas están vacías, imprime un mensaje y devuelve `None`.
  - Complejidad: O(N) en el peor caso (cuando se necesita transferir elementos), pero O(1) amortizado.

- **Método `front()`**:
  - Si `pila_salida` está vacía, transfiere todos los elementos de `pila_entrada` a `pila_salida`.
  - Devuelve el elemento en el tope de `pila_salida` sin eliminarlo.
  - Si ambas pilas están vacías, imprime un mensaje y devuelve `None`.
  - Complejidad: O(N) en el peor caso, pero O(1) amortizado.

- **Método `mostrar_cola()`**:
  - Muestra los elementos de la cola en orden (de frente a final).
  - Recorre `pila_salida` en orden inverso y luego `pila_entrada`.
  - Complejidad: O(N), donde N es el número de elementos en la cola.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Operaciones Realizadas**
1. **Enqueue**:
   - Insertamos elementos: `10`, `20`, `30`.
   - Resultado: `pila_entrada = [10, 20, 30]`, `pila_salida = []`.

2. **Mostrar Cola**:
   ```
   Contenido de la cola (de frente a final):
   10
   20
   30
   ```

3. **Front**:
   - Transferimos elementos de `pila_entrada` a `pila_salida`: `pila_salida = [30, 20, 10]`.
   - Obtenemos el elemento en el frente: `10`.

4. **Dequeue**:
   - Eliminamos el elemento en el frente (`10`): `pila_salida = [30, 20]`.
   - Eliminamos el siguiente elemento en el frente (`20`): `pila_salida = [30]`.

5. **Mostrar Cola Actualizada**:
   ```
   Contenido de la cola (de frente a final):
   30
   ```

6. **Intentar Dequeue sin Elementos**:
   - Intentamos eliminar un elemento cuando la cola está vacía.
   - Mensaje: "La cola está vacía. No se puede eliminar ningún elemento."

### **⏱️ Complejidad Temporal**
1. **Enqueue**:
   - Complejidad: O(1), ya que `append` es eficiente en Python.

2. **Dequeue**:
   - Complejidad: O(N) en el peor caso (cuando se necesita transferir elementos), pero O(1) amortizado.

3. **Front**:
   - Complejidad: O(N) en el peor caso, pero O(1) amortizado.

4. **Mostrar Cola**:
   - Complejidad: O(N), donde N es el número de elementos en la cola.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza **dos pilas** para implementar una cola.
   - Las operaciones `enqueue`, `dequeue` y `front` son compatibles con esta estructura.

2. **Por Qué Se Usaron Dos Pilas**:
   - Las pilas son ideales para este problema porque permiten invertir el orden de los elementos al transferirlos entre `pila_entrada` y `pila_salida`.
   - Esto permite simular el comportamiento FIFO de una cola.

3. **Eficiencia**:
   - Complejidad temporal: O(1) amortizado para `enqueue`, `dequeue` y `front`; O(N) para mostrar la cola.
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
