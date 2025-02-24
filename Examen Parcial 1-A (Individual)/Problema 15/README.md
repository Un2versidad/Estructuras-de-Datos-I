![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 15: Sistema de Entrega de Pedidos**

## **📖 Descripción del Problema**
Una empresa de entregas tiene un sistema donde recibe pedidos de clientes y los asigna a repartidores. Los pedidos pueden ser normales o urgentes:
- Los pedidos urgentes deben ser atendidos primero.
- Los pedidos normales se atienden en el orden en que llegan.
- Cada repartidor solo puede llevar un pedido a la vez.
- Se debe permitir agregar y procesar pedidos de manera eficiente. 

Requisitos:
- Diseñar una estructura de datos eficiente para gestionar los pedidos.
- Implementar funciones para agregar un pedido, asignar un pedido a un repartidor y mostrar los pedidos pendientes.
- El sistema debe permitir múltiples repartidores.

## **❓Para resolverlo, deberá responder las siguientes preguntas**

### **1. ¿Qué estructura de datos permite manejar prioridades?**
- **Respuesta**:  
  Una **cola de prioridad** (implementada con un **heap**) es ideal para manejar elementos con diferentes niveles de prioridad. En Python, se puede utilizar el módulo `heapq` para implementar un heap, donde los elementos con menor valor tienen mayor prioridad.  
  - **Razón**: Los heaps permiten insertar y extraer elementos en tiempo logarítmico ($ O(\log N) $), lo que es eficiente para manejar prioridades.

### **2. ¿Cómo se podría organizar la cola para que los pedidos urgentes sean atendidos primero?**
- **Respuesta**:  
  Los pedidos pueden organizarse en una **cola de prioridad** utilizando un heap. Los pedidos urgentes reciben una prioridad más alta (valor menor en el heap), mientras que los pedidos normales reciben una prioridad más baja (valor mayor). Al extraer elementos del heap, los pedidos urgentes siempre serán atendidos primero.  
  - **Ejemplo**:  
    - Prioridad `1`: Pedido urgente.
    - Prioridad `2`: Pedido normal.

### **3. ¿Cómo se asignan pedidos a los repartidores de manera eficiente?**
- **Respuesta**:  
  Los repartidores disponibles se gestionan mediante una **cola** (implementada con `deque`). Cuando un pedido debe ser asignado, se selecciona al primer repartidor disponible en la cola. Esta estrategia asegura que los repartidores sean asignados en el orden en que están disponibles, garantizando equidad y eficiencia.  
  - **Razón**: Las colas son ideales para este problema porque permiten manejar elementos en orden FIFO (primero en entrar, primero en salir).

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Cola de Prioridad (`heapq`)**:
   - Se utiliza un **heap** (montículo) para manejar los pedidos con prioridad.
   - Los pedidos urgentes tienen prioridad más alta (valor menor en el heap).

2. **Cola (`deque`)**:
   - Se utiliza una cola para gestionar los repartidores disponibles.
   - Los repartidores se asignan en el orden en que están disponibles.

3. **Clase `SistemaEntrega`**:
   - Implementa el sistema de entrega utilizando las estructuras de datos mencionadas.
   - Contiene métodos para agregar pedidos, agregar repartidores, asignar pedidos y mostrar pedidos pendientes.

### **💻 Explicación del Código**

#### **Clase `SistemaEntrega`**
- **Constructor (`__init__`)**:
  - Inicializa una cola de prioridad (`pedidos`) para almacenar los pedidos.
  - Inicializa una cola (`repartidores_disponibles`) para almacenar los repartidores disponibles.
  - Usa un contador (`id_pedido_actual`) para generar identificadores únicos para los pedidos.

- **Método `agregar_pedido(descripcion, es_urgente)`**:
  - Agrega un pedido al heap con su prioridad correspondiente:
    - Prioridad `1` para pedidos urgentes.
    - Prioridad `2` para pedidos normales.
  - Complejidad: $ O(\log N) $, donde $ N $ es el número de pedidos en el heap.

- **Método `agregar_repartidor(nombre)`**:
  - Agrega un repartidor a la cola de repartidores disponibles.
  - Complejidad: $ O(1) $, ya que `append` es eficiente en `deque`.

- **Método `asignar_pedido()`**:
  - Asigna el próximo pedido disponible (según la prioridad) al primer repartidor disponible.
  - Si no hay pedidos o repartidores disponibles, imprime un mensaje.
  - Complejidad: $ O(\log N) $ para extraer el pedido del heap y $ O(1) $ para asignar un repartidor.

- **Método `mostrar_pedidos_pendientes()`**:
  - Muestra los pedidos pendientes en orden de prioridad.
  - Complejidad: $ O(N \log N) $, donde $ N $ es el número de pedidos, debido a la ordenación.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Operaciones Realizadas**
1. **Agregar Pedidos**:
   - Pedido 1: "Entregar paquete a Juan" (Urgente).
   - Pedido 2: "Entregar comida a María" (Normal).
   - Pedido 3: "Entregar documentos a Carlos" (Urgente).

2. **Agregar Repartidores**:
   - Repartidor A.
   - Repartidor B.

3. **Mostrar Pedidos Pendientes**:
   ```
   Pedidos pendientes (ordenados por prioridad):
   - ID: 1, Descripción: Entregar paquete a Juan, Tipo: Urgente
   - ID: 3, Descripción: Entregar documentos a Carlos, Tipo: Urgente
   - ID: 2, Descripción: Entregar comida a María, Tipo: Normal
   ```

4. **Asignar Pedidos**:
   - Pedido 1: "Entregar paquete a Juan" → Repartidor A.
   - Pedido 3: "Entregar documentos a Carlos" → Repartidor B.

5. **Mostrar Pedidos Pendientes Después de Asignar**:
   ```
   Pedidos pendientes (ordenados por prioridad):
   - ID: 2, Descripción: Entregar comida a María, Tipo: Normal
   ```

6. **Intentar Asignar sin Repartidores Disponibles**:
   - Mensaje: "No hay repartidores disponibles."

### **⏱️ Complejidad Temporal**
1. **Agregar Pedido**:
   - Complejidad: $ O(\log N) $, donde $ N $ es el número de pedidos en el heap.

2. **Agregar Repartidor**:
   - Complejidad: $ O(1) $, ya que `append` es eficiente en `deque`.

3. **Asignar Pedido**:
   - Complejidad: $ O(\log N) $ para extraer el pedido del heap y $ O(1) $ para asignar un repartidor.

4. **Mostrar Pedidos Pendientes**:
   - Complejidad: $ O(N \log N) $, donde $ N $ es el número de pedidos, debido a la ordenación.

---

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza un **heap** para manejar prioridades y una **cola** para gestionar repartidores.
   - Las operaciones de agregar, asignar y mostrar pedidos son compatibles con estas estructuras.

2. **Por Qué Se Usó un Heap y una Cola**:
   - El heap permite manejar pedidos con prioridad de manera eficiente.
   - La cola permite asignar repartidores en el orden en que están disponibles.

3. **Eficiencia**:
   - Complejidad temporal: $ O(\log N) $ para agregar y asignar pedidos; $ O(N \log N) $ para mostrar pedidos pendientes.
   - Complejidad espacial: $ O(N + M) $, donde $ N $ es el número de pedidos y $ M $ es el número de repartidores.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Pedido agregado: Entregar paquete a Juan (Prioridad: Urgente)
Pedido agregado: Entregar comida a María (Prioridad: Normal)
Pedido agregado: Entregar documentos a Carlos (Prioridad: Urgente)
Repartidor 'Repartidor A' agregado al sistema.
Repartidor 'Repartidor B' agregado al sistema.
Mostrar pedidos pendientes:
Pedidos pendientes (ordenados por prioridad):
- ID: 1, Descripción: Entregar paquete a Juan, Tipo: Urgente
- ID: 3, Descripción: Entregar documentos a Carlos, Tipo: Urgente
- ID: 2, Descripción: Entregar comida a María, Tipo: Normal
Asignar pedidos:
Pedido asignado: 'Entregar paquete a Juan' -> Repartidor: Repartidor A
Pedido asignado: 'Entregar documentos a Carlos' -> Repartidor: Repartidor B
Mostrar pedidos pendientes después de asignar:
Pedidos pendientes (ordenados por prioridad):
- ID: 2, Descripción: Entregar comida a María, Tipo: Normal
No hay repartidores disponibles.
```
