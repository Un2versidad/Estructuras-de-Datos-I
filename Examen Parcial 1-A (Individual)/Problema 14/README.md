![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 14: Detección de Ciclos en una Lista Enlazada**

## **📖 Descripción del Problema**
Dada una lista enlazada con un posible ciclo, escribe un algoritmo que detecte si la lista tiene un ciclo o no (algoritmo de Floyd, "tortuga y liebre").

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `Nodo`**:
   - Representa un nodo en la lista enlazada.
   - Contiene dos atributos:
     - `valor`: El valor almacenado en el nodo.
     - `siguiente`: Una referencia al siguiente nodo.

2. **Función `tiene_ciclo(cabeza)`**:
   - Implementa el **algoritmo de Floyd** (también conocido como "tortuga y liebre") para detectar ciclos.
   - Usa dos punteros (`tortuga` y `liebre`) que avanzan a diferentes velocidades:
     - `tortuga` avanza un nodo por iteración.
     - `liebre` avanza dos nodos por iteración.
   - Si los punteros coinciden en algún momento, significa que hay un ciclo.

### **💻 Explicación del Código**

#### **Clase `Nodo`**
- **Constructor (`__init__`)**:
  - Inicializa el valor del nodo y establece `siguiente` como `None`.

#### **Función `tiene_ciclo(cabeza)`**
- **Verificación inicial**:
  - Si la lista está vacía o tiene un solo nodo, no puede haber ciclo.

- **Algoritmo de Floyd**:
  - Se inicializan dos punteros (`tortuga` y `liebre`) en la cabeza de la lista.
  - En cada iteración:
    - `tortuga` avanza un nodo.
    - `liebre` avanza dos nodos.
  - Si `tortuga` y `liebre` coinciden, se detecta un ciclo.
  - Si `liebre` o `liebre.siguiente` es `None`, se llega al final de la lista y no hay ciclo.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Lista con Ciclo**
1. **Estructura de la Lista**:
   ```
   nodo1 -> nodo2 -> nodo3 -> nodo4
                 ^              |
                 |______________|
   ```

2. **Iteraciones del Algoritmo**:
   - Iteración 1:
     - `tortuga`: nodo2
     - `liebre`: nodo3
   - Iteración 2:
     - `tortuga`: nodo3
     - `liebre`: nodo3 (coinciden)
   - Resultado: La lista tiene un ciclo.

#### **Lista sin Ciclo**
1. **Estructura de la Lista**:
   ```
   nodo5 -> nodo6 -> nodo7 -> None
   ```

2. **Iteraciones del Algoritmo**:
   - Iteración 1:
     - `tortuga`: nodo6
     - `liebre`: nodo7
   - Iteración 2:
     - `tortuga`: nodo7
     - `liebre`: None (fin de la lista)
   - Resultado: La lista no tiene un ciclo.

### **⏱️ Complejidad Temporal**
1. **Algoritmo de Floyd**:
   - Complejidad: O(N), donde N es el número de nodos en la lista.
   - Explicación: Los punteros recorren la lista una vez, avanzando a diferentes velocidades.

2. **Espacial**:
   - Complejidad: O(1), ya que solo se utilizan dos punteros adicionales (`tortuga` y `liebre`).

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza una **lista enlazada** implementada con nodos.
   - Cada nodo se representa mediante una **clase tradicional** (`Nodo`).

2. **Por Qué Se Usó el Algoritmo de Floyd**:
   - El algoritmo de Floyd es ideal para este problema porque detecta ciclos de manera eficiente en tiempo lineal y con espacio constante.

3. **Eficiencia**:
   - Complejidad temporal: O(N).
   - Complejidad espacial: O(1).

### **📢 Salida del Código**
Observa la salida en la consola:
```
La lista tiene un ciclo.
La lista no tiene un ciclo.
```
