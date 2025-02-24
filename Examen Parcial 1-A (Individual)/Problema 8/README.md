![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 8: Invertir una Lista Doblemente Enlazada**

## **📖 Descripción del Problema**
Dada una lista doblemente enlazada de números enteros, escribir una función que invierta el orden de los nodos en la lista.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `Nodo`**:
   - Representa un nodo en la lista doblemente enlazada.
   - Contiene tres atributos:
     - `valor`: El valor almacenado en el nodo.
     - `anterior`: Una referencia al nodo anterior.
     - `siguiente`: Una referencia al siguiente nodo.

2. **Clase `ListaDoblementeEnlazada`**:
   - Implementa la lista doblemente enlazada.
   - Contiene métodos para insertar nodos, mostrar la lista y revertirla.

### **💻 Explicación del Código**

#### **Clase `Nodo`**
- **Constructor (`__init__`)**:
  - Inicializa el valor del nodo y establece `anterior` y `siguiente` como `None`.

#### **Clase `ListaDoblementeEnlazada`**
- **Constructor (`__init__`)**:
  - Inicializa la lista con `cabeza` y `cola` como `None`, indicando que la lista está vacía.

- **Método `insertar_al_final(valor)`**:
  - Crea un nuevo nodo con el valor dado.
  - Si la lista está vacía, asigna el nuevo nodo como tanto la cabeza como la cola.
  - Si no, conecta el nuevo nodo al final de la lista y actualiza la cola.

- **Método `mostrar_lista()`**:
  - Recorre la lista desde la cabeza e imprime los valores de los nodos en orden.

- **Método `invertir()`**:
  - Intercambia las referencias `anterior` y `siguiente` de cada nodo.
  - Al finalizar, intercambia las referencias de `cabeza` y `cola` para completar la inversión.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Operaciones Realizadas**
1. **Insertar Nodos**:
   - Insertamos nodos con valores `10`, `20`, `30` y `40`.
   - Resultado: `10 <-> 20 <-> 30 <-> 40 -> None`.

2. **Mostrar Lista Original**:
   ```
   Contenido de la lista:
   10 <-> 20 <-> 30 <-> 40 -> None
   ```

3. **Invertir la Lista**:
   - Intercambiamos las referencias `anterior` y `siguiente` de cada nodo.
   - Resultado: `40 <-> 30 <-> 20 <-> 10 -> None`.

4. **Mostrar Lista Invertida**:
   ```
   Contenido de la lista:
   40 <-> 30 <-> 20 <-> 10 -> None
   ```
   
### **⏱️ Complejidad Temporal**
1. **Insertar al Final**:
   - Complejidad: O(1), ya que se agrega el nodo directamente al final utilizando la referencia `cola`.

2. **Mostrar Lista**:
   - Complejidad: O(N), donde N es el número de nodos en la lista, ya que se recorre toda la lista para imprimir los valores.

3. **Invertir Lista**:
   - Complejidad: O(N), ya que se recorre la lista una sola vez para intercambiar las referencias `anterior` y `siguiente`.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza una **lista doblemente enlazada** implementada con nodos y referencias bidireccionales.
   - Cada nodo se representa mediante una **clase tradicional** (`Nodo`).

2. **Por Qué Se Usó una Lista Doblemente Enlazada**:
   - Las listas doblemente enlazadas son ideales para este problema porque permiten recorrer la lista en ambas direcciones, lo cual facilita la inversión.

3. **Eficiencia**:
   - Complejidad temporal: O(N) para invertir la lista.
   - Complejidad espacial: O(1), ya que no se utilizan estructuras adicionales aparte de las variables temporales.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Lista original:
Contenido de la lista:
10 <-> 20 <-> 30 <-> 40 -> None
Lista invertida:
Contenido de la lista:
40 <-> 30 <-> 20 <-> 10 -> None
```
