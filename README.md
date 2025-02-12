![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# 📚 **Estructuras de Datos I - (UIP)** 🧠

[![Awesome](https://img.shields.io/badge/Data-Structures-brightgreen)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://opensource.org/licenses/MIT)

## 📑 **Índice**

1. [¿Qué es una Estructura de Datos?](#-qué-es-una-estructura-de-datos)
2. [Arreglo (Array)](#-arreglo-array)
3. [Lista Enlazada Simple](#-lista-enlazada-simple)
4. [Lista Enlazada Doble](#-lista-enlazada-doble)
5. [Pila (Stack)](#-pila-stack)
6. [Cola (Queue)](#-cola-queue)
7. [Árbol Binario (Binary Tree)](#-árbol-binario-binary-tree)
8. [Grafo (Graph)](#-grafo-graph)
9. [Tabla Hash (Hash Table)](#-tabla-hash-hash-table)
10. [Montículo (Heap)](#-montículo-heap)
11. [Conjunto Disjunto (Disjoint Set)](#-conjunto-disjunto-disjoint-set)

## 🤔 **¿Qué es una Estructura de Datos?**

Una **estructura de datos** 🧱 es una forma de organizar y almacenar datos en un programa de computadora de manera que se puedan acceder y modificar de forma eficiente. Las estructuras de datos son fundamentales para resolver problemas computacionales, ya que permiten optimizar el uso de memoria 💾, mejorar el rendimiento de los algoritmos ⚡️ y facilitar la manipulación de datos.

Existen diferentes tipos de estructuras de datos, cada una diseñada para resolver problemas específicos. A continuación, describiremos algunas de las estructuras de datos más comunes, su funcionamiento y sus representaciones gráficas en ASCII art ✨.

---

## 🔢 **Arreglo (Array)**

### Descripción:
Un **arreglo** 📊 es una colección de elementos del mismo tipo almacenados en memoria contigua. Cada elemento se puede acceder directamente mediante un índice.

### Funcionamiento:
- **Acceso**: O(1) (acceso constante por índice).
- **Inserción/eliminación**: O(n) (puede requerir desplazamiento de elementos).

### Representación Gráfica:

```
+-----+-----+-----+-----+-----+
|  1  |  2  |  3  |  4  |  5  |
+-----+-----+-----+-----+-----+
   0     1     2     3     4
```

---

## 🔗 **Lista Enlazada Simple**

### Descripción:
Una **lista enlazada simple** 🖇️ es una colección de nodos donde cada nodo contiene un valor y una referencia al siguiente nodo en la secuencia. El último nodo apunta a `NULL`, indicando el final de la lista.

### Funcionamiento:
- **Acceso**: O(n) (se debe recorrer la lista para llegar a un nodo específico).
- **Inserción/eliminación**: O(1) si se conoce el nodo previo, O(n) en caso contrario.

### Representación Gráfica:

```
CABEZA
   |
   v
+-----+    +-----+    +-----+    +-----+
|  1  |--->|  2  |--->|  3  |--->|  4  |---> NULL
+-----+    +-----+    +-----+    +-----+
```

> **Nota:** En una lista enlazada simple, cada nodo solo tiene una referencia al siguiente nodo, lo que permite recorrer la lista en una sola dirección ➡️.

---

## ↔️ **Lista Enlazada Doble**

### Descripción:
Una **lista enlazada doble** ↔️ es similar a una lista enlazada simple, pero cada nodo tiene dos referencias: una al nodo anterior y otra al siguiente. Esto permite recorrer la lista en ambas direcciones.

### Funcionamiento:
- **Acceso**: O(n) (se debe recorrer la lista para llegar a un nodo específico).
- **Inserción/eliminación**: O(1) si se conoce el nodo previo o siguiente, O(n) en caso contrario.

### Representación Gráfica:

```
CABEZA                                                                 COLA
   |                                                                      |
   v                                                                      v
+-----+    <---+    +-----+    <---+    +-----+    <---+    +-----+    <---+
|  1  |--------|--->|  2  |--------|--->|  3  |--------|--->|  4  |--------|---> NULL
+-----+        +--->+-----+        +--->+-----+        +--->+-----+        +--->
```

> **Nota:** En una lista enlazada doble, cada nodo tiene una referencia al nodo anterior y al siguiente, lo que permite recorrer la lista en ambas direcciones ↔️.

---

## 📦 **Pila (Stack)**

### Descripción:
Una **pila** 📚 es una estructura de datos **LIFO** (**Último en Entrar, Primero en Salir**). Los elementos se añaden y eliminan desde la parte superior de la pila.

### Funcionamiento:
- **Push (añadir)**: O(1).
- **Pop (eliminar)**: O(1).

### Representación Gráfica:

```
TOPE
  |
  v
+-----+
|  4  |
+-----+
|  3  |
+-----+
|  2  |
+-----+
|  1  |
+-----+
```

> **Nota:** En una pila, el último elemento que entra es el primero en salir. Esto se conoce como **LIFO** (Last In, First Out) ⬆️⬇️.

---

## 🚶‍♂️ **Cola (Queue)**

### Descripción:
Una **cola** 🚶‍♀️ es una estructura de datos **FIFO** (**Primero en Entrar, Primero en Salir**). Los elementos se añaden al final y se eliminan desde el frente.

### Funcionamiento:
- **Enqueue (añadir)**: O(1).
- **Dequeue (eliminar)**: O(1).

### Representación Gráfica:

```
FRENTE                          FINAL
   |                              |
   v                              v
+-----+    +-----+    +-----+    +-----+
|  1  |--->|  2  |--->|  3  |--->|  4  |---> NULL
+-----+    +-----+    +-----+    +-----+
```

> **Nota:** En una cola, el primer elemento que entra es el primero en salir. Esto se conoce como **FIFO** (First In, First Out) ➡️⬅️.

---

## 🌳 **Árbol Binario (Binary Tree)**

### Descripción:
Un **árbol binario** 🌲 es una estructura jerárquica donde cada nodo tiene como máximo dos hijos: izquierdo y derecho.

### Funcionamiento:
- **Búsqueda**: O(log n) en árboles balanceados.
- **Inserción/eliminación**: O(log n) en árboles balanceados.

### Representación Gráfica:

```
         RAÍZ
          (5)
         /   \
      (3)     (8)
     /   \       \
   (1)   (4)     (9)
```

---

## 🕸️ **Grafo (Graph)**

### Descripción:
Un **grafo** 🕸️ es una colección de nodos (vértices) conectados por aristas. Pueden ser dirigidos o no dirigidos.

### Funcionamiento:
- **Recorrido**: BFS (Búsqueda en Anchura), DFS (Búsqueda en Profundidad).
- **Representación**: Matriz de adyacencia o lista de adyacencia.

### Representación Gráfica:

```
    (A) --- (B)
     |       |
     |       |
    (C) --- (D)
```

---

## 🔑 **Tabla Hash (Hash Table)**

### Descripción:
Una **tabla hash** 🔑 es una estructura de datos que asocia claves con valores. Utiliza una función hash para calcular un índice donde se almacena el valor.

### Funcionamiento:
- **Inserción/búsqueda/eliminación**: O(1) en promedio, O(n) en el peor caso (colisiones).

### Representación Gráfica:

```
ÍNDICE   VALOR
   0     "manzana"
   1     "banana"
   2     "cereza"
   3     NULL
   4     "dátil"
```

---

## 🏔️ **Montículo (Heap)**

### Descripción:
Un **montículo** 🏔️ es un árbol binario completo donde cada nodo cumple con la propiedad del montículo (mínimo o máximo).

### Funcionamiento:
- **Inserción/eliminación**: O(log n).
- **Acceso al mínimo/máximo**: O(1).

### Representación Gráfica (Montículo Mínimo):

```
         (1)
        /   \
     (2)     (3)
    /   \    /
  (4)  (5) (6)
```

---

## 🔄 **Conjunto Disjunto (Disjoint Set)**

### Descripción:
Un **conjunto disjunto** 🔄 es una estructura que mantiene una colección de conjuntos disjuntos y permite operaciones de unión y búsqueda eficientes.

### Funcionamiento:
- **Find**: O(α(n)) (casi constante con compresión de ruta).
- **Union**: O(α(n)).

### Representación Gráfica:

```
Conjunto 1: {1, 2, 3}
Conjunto 2: {4, 5}
Conjunto 3: {6}

Representación como árboles:
  1       4       6
 / \     /
2   3   5
```
