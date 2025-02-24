![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 9: Implementación de una Pila con un Arreglo Dinámico**

## **📖 Descripción del Problema**
Implementar una pila utilizando un arreglo dinámico que permita realizar las siguientes operaciones:
1. **`push(x)`**: Agregar un elemento al tope de la pila.
2. **`pop()`**: Eliminar el elemento en el tope de la pila.
3. **`top()`**: Obtener el elemento en el tope de la pila sin eliminarlo.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `Pila`**:
   - Implementa una pila utilizando un **arreglo dinámico** (`list` en Python).
   - Contiene métodos para realizar las operaciones `push`, `pop`, `top` y mostrar el contenido de la pila.

### **💻 Explicación del Código**

#### **Clase `Pila`**
- **Constructor (`__init__`)**:
  - Inicializa un arreglo vacío (`self.arreglo`) para almacenar los elementos de la pila.

- **Método `push(x)`**:
  - Agrega un elemento al final del arreglo, que representa el tope de la pila.
  - Complejidad: O(1) en promedio, ya que `append` es eficiente en Python.

- **Método `pop()`**:
  - Elimina y devuelve el último elemento del arreglo, que representa el tope de la pila.
  - Si la pila está vacía, imprime un mensaje y devuelve `None`.
  - Complejidad: O(1) en promedio, ya que `pop` es eficiente en Python.

- **Método `top()`**:
  - Devuelve el último elemento del arreglo sin eliminarlo.
  - Si la pila está vacía, imprime un mensaje y devuelve `None`.
  - Complejidad: O(1), ya que acceder al último elemento de un arreglo es directo.

- **Método `mostrar_pila()`**:
  - Recorre el arreglo desde el final hacia el inicio e imprime los elementos.
  - Complejidad: O(N), donde N es el número de elementos en la pila.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Operaciones Realizadas**
1. **Push**:
   - Insertamos elementos `10`, `20` y `30`.
   - Resultado: `[10, 20, 30]` (el tope es `30`).

2. **Mostrar Pila**:
   ```
   Contenido de la pila (de tope a base):
   30
   20
   10
   ```

3. **Top**:
   - Obtenemos el elemento en el tope: `30`.

4. **Pop**:
   - Eliminamos el elemento en el tope (`30`).
   - Resultado: `[10, 20]` (el tope es `20`).
   - Eliminamos el siguiente elemento en el tope (`20`).
   - Resultado: `[10]` (el tope es `10`).

5. **Mostrar Pila Actualizada**:
   ```
   Contenido de la pila (de tope a base):
   10
   ```

6. **Pop en Pila Vacía**:
   - Intentamos eliminar un elemento cuando la pila está vacía.
   - Mensaje: "La pila está vacía. No se puede eliminar ningún elemento."

### **⏱️ Complejidad Temporal**
1. **Push**:
   - Complejidad: O(1) en promedio, ya que `append` es eficiente en Python.

2. **Pop**:
   - Complejidad: O(1) en promedio, ya que `pop` es eficiente en Python.

3. **Top**:
   - Complejidad: O(1), ya que acceder al último elemento de un arreglo es directo.

4. **Mostrar Pila**:
   - Complejidad: O(N), donde N es el número de elementos en la pila.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza un **arreglo dinámico** (`list` en Python) para implementar la pila.
   - Las operaciones `push`, `pop` y `top` son compatibles con esta estructura.

2. **Por Qué Se Usó un Arreglo Dinámico**:
   - Los arreglos dinámicos son ideales para este problema porque permiten inserciones y eliminaciones eficientes en el tope de la pila.
   - No se necesitan estructuras adicionales como listas enlazadas, ya que los arreglos dinámicos ya están optimizados para estas operaciones.

3. **Eficiencia**:
   - Complejidad temporal: O(1) para `push`, `pop` y `top`; O(N) para mostrar la pila.
   - Complejidad espacial: O(N), donde N es el número de elementos en la pila.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Elemento 10 agregado a la pila.
Elemento 20 agregado a la pila.
Elemento 30 agregado a la pila.
Pila después de push:
Contenido de la pila (de tope a base):
30
20
10
Elemento en el tope: 30
Elemento 30 eliminado de la pila.
Elemento 20 eliminado de la pila.
Pila después de pop:
Contenido de la pila (de tope a base):
10
Elemento 10 eliminado de la pila.
La pila está vacía. No se puede eliminar ningún elemento.
```
