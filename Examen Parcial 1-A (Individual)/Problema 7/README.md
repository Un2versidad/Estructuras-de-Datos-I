![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 7: Lista Simplemente Enlazada**

## **📖 Descripción del Problema**
Implementar una lista simplemente enlazada que permita realizar las siguientes operaciones:
1. **Insertar un nodo al inicio**.
2. **Insertar un nodo al final**.
3. **Buscar un nodo por su valor**.
4. **Eliminar un nodo por su valor**.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `Nodo`**:
   - Representa un nodo en la lista simplemente enlazada.
   - Contiene dos atributos:
     - `valor`: El valor almacenado en el nodo.
     - `siguiente`: Una referencia al siguiente nodo en la lista.

2. **Clase `ListaEnlazada`**:
   - Implementa la lista simplemente enlazada.
   - Contiene métodos para insertar, buscar, eliminar y mostrar nodos.

### **💻 Explicación del Código**

#### **Clase `Nodo`**
- **Constructor (`__init__`)**:
  - Inicializa el valor del nodo y establece `siguiente` como `None`.

#### **Clase `ListaEnlazada`**
- **Constructor (`__init__`)**:
  - Inicializa la lista con `cabeza` como `None`, indicando que la lista está vacía.

- **Método `insertar_al_inicio(valor)`**:
  - Crea un nuevo nodo con el valor dado.
  - Asigna el nodo actual como el siguiente del nuevo nodo.
  - Actualiza la cabeza de la lista al nuevo nodo.

- **Método `insertar_al_final(valor)`**:
  - Crea un nuevo nodo con el valor dado.
  - Si la lista está vacía, asigna el nuevo nodo como la cabeza.
  - Si no, recorre la lista hasta el último nodo y lo conecta al nuevo nodo.

- **Método `buscar(valor)`**:
  - Recorre la lista desde la cabeza hasta encontrar un nodo con el valor buscado.
  - Si lo encuentra, imprime un mensaje y devuelve el nodo.
  - Si no lo encuentra, imprime un mensaje y devuelve `None`.

- **Método `eliminar(valor)`**:
  - Si la lista está vacía, imprime un mensaje y termina.
  - Si el nodo a eliminar es la cabeza, actualiza la cabeza al siguiente nodo.
  - Si no, recorre la lista para encontrar el nodo y lo elimina ajustando las referencias.

- **Método `mostrar_lista()`**:
  - Recorre la lista desde la cabeza e imprime los valores de los nodos en orden.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Operaciones Realizadas**
1. **Insertar al Inicio**:
   - Insertamos nodos con valores `20` y `10`.
   - Resultado: `20 -> 10 -> None`.

2. **Insertar al Final**:
   - Insertamos nodos con valores `30` y `40`.
   - Resultado: `20 -> 10 -> 30 -> 40 -> None`.

3. **Mostrar Lista**:
   ```
   Contenido de la lista:
   20 -> 10 -> 30 -> 40 -> None
   ```

4. **Buscar Nodos**:
   - Buscamos el valor `30`: Nodo encontrado.
   - Buscamos el valor `50`: Nodo no encontrado.

5. **Eliminar Nodos**:
   - Eliminamos el valor `20`: Nodo eliminado (era la cabeza).
   - Eliminamos el valor `50`: Nodo no encontrado.

6. **Mostrar Lista Actualizada**:
   ```
   Contenido de la lista:
   10 -> 30 -> 40 -> None
   ```

### **⏱️ Complejidad Temporal**
1. **Insertar al Inicio**:
   - Complejidad: O(1), ya que solo se modifica la cabeza de la lista.

2. **Insertar al Final**:
   - Complejidad: O(N), donde N es el número de nodos en la lista, ya que se recorre toda la lista para llegar al final.

3. **Buscar un Nodo**:
   - Complejidad: O(N), ya que se recorre la lista hasta encontrar el nodo o llegar al final.

4. **Eliminar un Nodo**:
   - Complejidad: O(N), ya que se recorre la lista hasta encontrar el nodo a eliminar.

5. **Mostrar Lista**:
   - Complejidad: O(N), ya que se recorre toda la lista para imprimir los valores.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza una **lista simplemente enlazada** implementada con nodos y referencias.
   - Cada nodo se representa mediante una **clase tradicional** (`Nodo`).

2. **Por Qué Se Usó una Lista Enlazada**:
   - Las listas enlazadas son ideales para este problema porque permiten inserciones y eliminaciones eficientes en el inicio y el final.
   - No se necesitan estructuras adicionales como arreglos, pilas o colas, ya que las listas enlazadas están diseñadas específicamente para estas operaciones.

3. **Eficiencia**:
   - Complejidad temporal: O(1) para inserciones al inicio; O(N) para inserciones al final, búsquedas y eliminaciones.
   - Complejidad espacial: O(N), donde N es el número de nodos en la lista.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Nodo con valor 10 insertado al inicio.
Nodo con valor 20 insertado al inicio.
Nodo con valor 30 insertado al final.
Nodo con valor 40 insertado al final.
Contenido de la lista:
20 -> 10 -> 30 -> 40 -> None
Nodo con valor 30 encontrado.
Nodo con valor 50 no encontrado.
Nodo con valor 20 eliminado (era la cabeza).
Nodo con valor 50 no encontrado para eliminar.
Contenido de la lista:
10 -> 30 -> 40 -> None
```
